import streamlit as st
from transformers import AutoTokenizer, AutoModel, DistilBertTokenizer, DistilBertModel
from pinecone import Pinecone, ServerlessSpec
import torch
from openai import OpenAI
from datetime import datetime
@@ -8,19 +9,38 @@
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client
def setup_openai():
    return OpenAI(api_key=OPENAI_API_KEY)

# Initialize the OpenAI client
client = setup_openai()
# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Define the index names
recipe_index_name = 'recipe-index'
restaurant_index_name = 'restaurant-index'

# Create the Pinecone indices if they do not exist
def setup_pinecone(index_name, dimension):
    if index_name not in pc.list_indexes().names():
        try:
            pc.create_index(
                name=index_name,
                dimension=dimension,
                metric='cosine',
                spec=ServerlessSpec(cloud='aws', region='us-east-1')
            )
        except Exception as e:
            st.error(f"Failed to create index: {e}")
    return pc.Index(index_name)

# Initialize Hugging Face models and tokenizers
recipe_tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
recipe_model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

restaurant_tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
restaurant_model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Initialize OpenAI client
def setup_openai():
    return OpenAI(api_key=OPENAI_API_KEY)

# Functions for embedding generation
def get_embedding(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
@@ -34,10 +54,22 @@ def convert_text_to_embedding(text):
def get_restaurant_embedding(text):
    return get_embedding(text, restaurant_tokenizer, restaurant_model)

# Initialize Pinecone indices
recipe_index = setup_pinecone(recipe_index_name, 768)
restaurant_index = setup_pinecone(restaurant_index_name, 768)

# Initialize the OpenAI client
client = setup_openai()

# Function to query Pinecone for recipes
def fetch_recipe_metadata(user_query):
    # Add logic to query Pinecone and fetch recipes
    return []
    query_vector = convert_text_to_embedding(user_query)
    response = recipe_index.query(vector=query_vector, top_k=10, include_metadata=True)

    matches = response.get('matches', [])
    filtered_recipes = [match.get('metadata', {}) for match in matches if all(ingredient.lower() in match.get('metadata', {}).get('ingredients', '').lower() for ingredient in user_query.split(', '))]

    return filtered_recipes

# Function to generate a new recipe using OpenAI
def create_new_recipe(ingredients):
@@ -56,21 +88,25 @@ def create_new_recipe(ingredients):
# Function to query Pinecone for restaurants
def get_restaurant_metadata(description):
    embedding = get_restaurant_embedding(description)
    # Add logic to query Pinecone and fetch restaurants
    return []
    response = restaurant_index.query(
        vector=embedding,
        top_k=10,
        include_metadata=True
    )
    return response['matches'] if response['matches'] else []

# Function to filter messages
def is_relevant_message(content):
    food_related_keywords = ['recipe', 'food', 'ingredients', 'cook', 'cuisine', 'dish', 'meal', 'restaurant']
    return any(keyword in content.lower() for keyword in food_related_keywords)

# Function to process chat messages
def process_message(chat_input):
    if chat_input.strip():
        user_message = {"role": "user", "content": chat_input.strip()}
def process_message(input_text):
    if input_text.strip():
        user_message = {"role": "user", "content": input_text.strip()}
        st.session_state.messages.append(user_message)

        if is_relevant_message(chat_input.strip()):
        if is_relevant_message(input_text.strip()):
            response = fetch_model_response(st.session_state.messages)
        else:
            response = "This is not a relevant topic. Please ask about recipes or food-related queries."
@@ -100,26 +136,28 @@ def save_conversation():

# Main function for the Streamlit app
def main():
    st.sidebar.title("Menu")
    st.sidebar.title("Menu")  # Set the title for the sidebar
    menu_option = st.sidebar.selectbox("Select an Option", ["Find Recipes", "Find Restaurants", "Chat"])

    
    if menu_option == "Find Recipes":
        user_query = st.sidebar.text_input("Search for a recipe:", "")
        if user_query and (user_query != st.session_state.get('last_query', '')):
            st.session_state.last_query = user_query
            ingredients = user_query.split(', ')
            recipes = fetch_recipe_metadata(user_query)
            if recipes:
                st.session_state.recommended_recipes = [recipe for recipe in recipes][:3]
                st.session_state.recommended_recipes = [
                    recipe for recipe in recipes
                ][:3]
            else:
                st.session_state.recommended_recipes = [create_new_recipe(ingredients) for _ in range(3)]

            st.title("Recommended Recipes")
            if st.session_state.get('recommended_recipes'):
                for recipe in st.session_state.recommended_recipes:
                    st.write("*Name:* " + recipe['name'])
                    st.write("*Description:* " + recipe['description'])
                    st.write("*Steps:* " + recipe['steps'])
                    st.write("**Name:** " + recipe['name'])
                    st.write("**Description:** " + recipe['description'])
                    st.write("**Steps:** " + recipe['steps'])
                    st.markdown("---")
            else:
                st.write("No recommended recipes found.")
@@ -131,48 +169,52 @@ def main():
            if description:
                matches = get_restaurant_metadata(description)
                if matches:
                    st.write(f"*Restaurants Matching Description:*")
                    st.write(f"**Restaurants Matching Description:**")
                    for match in matches:
                        metadata = match['metadata']
                        st.write(f"*Name:* {metadata.get('name', 'N/A')}")
                        st.write(f"*Average Rating:* {metadata.get('averageRating', 'N/A')}")
                        st.write(f"*City:* {metadata.get('city', 'N/A')}")
                        st.write(f"*Description:* {metadata.get('description', 'N/A')}")
                        st.write(f"*Display Address:* {metadata.get('displayAddress', 'N/A')}")
                        st.write(f"*Image URL:* {metadata.get('imageUrl', 'N/A')}")
                        st.write(f"*Latitude:* {metadata.get('latitude', 'N/A')}")
                        st.write(f"*Longitude:* {metadata.get('longitude', 'N/A')}")
                        st.write(f"*Market:* {metadata.get('market', 'N/A')}")
                        st.write(f"*Price Range:* {metadata.get('priceRange', 'N/A')}")
                        st.write(f"*Rating Count:* {metadata.get('ratingCount', 'N/A')}")
                        st.write(f"*State:* {metadata.get('state', 'N/A')}")
                        st.write(f"*Street:* {metadata.get('street', 'N/A')}")
                        st.write(f"*Timezone:* {metadata.get('timezone', 'N/A')}")
                        st.write(f"*Zip Code:* {metadata.get('zipCode', 'N/A')}")
                        st.write(f"*Phone:* {metadata.get('phone', 'N/A')}")
                        st.write(f"*Website:* {metadata.get('website', 'N/A')}")
                        st.write(f"**Name:** {metadata.get('name', 'N/A')}")
                        st.write(f"**Average Rating:** {metadata.get('averageRating', 'N/A')}")
                        st.write(f"**City:** {metadata.get('city', 'N/A')}")
                        st.write(f"**Description:** {metadata.get('description', 'N/A')}")
                        st.write(f"**Display Address:** {metadata.get('displayAddress', 'N/A')}")
                        st.write(f"**Image URL:** {metadata.get('imageUrl', 'N/A')}")
                        st.write(f"**Latitude:** {metadata.get('latitude', 'N/A')}")
                        st.write(f"**Longitude:** {metadata.get('longitude', 'N/A')}")
                        st.write(f"**Market:** {metadata.get('market', 'N/A')}")
                        st.write(f"**Price Range:** {metadata.get('priceRange', 'N/A')}")
                        st.write(f"**Rating Count:** {metadata.get('ratingCount', 'N/A')}")
                        st.write(f"**State:** {metadata.get('state', 'N/A')}")
                        st.write(f"**Street:** {metadata.get('street', 'N/A')}")
                        st.write(f"**Timezone:** {metadata.get('timezone', 'N/A')}")
                        st.write(f"**Zip Code:** {metadata.get('zipCode', 'N/A')}")
                        st.write(f"**Phone:** {metadata.get('phone', 'N/A')}")
                        st.write(f"**Website URL:** {metadata.get('websiteUrl', 'N/A')}")
                        st.write(f"**Country:** {metadata.get('country', 'N/A')}")
                        st.write(f"**Cuisine Types:** {metadata.get('cuisineTypes', 'N/A')}")
                        st.write(f"**Price Levels:** {metadata.get('priceLevels', 'N/A')}")
                        st.write(f"**Dishes:** {metadata.get('dishes', 'N/A')}")
                        st.write(f"**Hours of Operation:** {metadata.get('hoursOfOperation', 'N/A')}")
                        st.write(f"**Tags:** {metadata.get('tags', 'N/A')}")
                        st.write(f"**Image URL:** {metadata.get('imageUrl', 'N/A')}")
                        st.write("---")
                else:
                    st.write("No restaurants found matching your description.")
                    st.write("No matching restaurants found.")

    elif menu_option == "Chat":
        if 'messages' not in st.session_state:
        if "messages" not in st.session_state:
            st.session_state.messages = []

        st.title("Chat with the Assistant")
        chat_input = st.text_input("You: ", key="chat_input")
        
        st.title("Chat with Assistant")
        user_input = st.text_input("You:", "")

        if st.button("Send"):
            process_message(chat_input)
            # Clear chat input using the key-based reset function
            st.session_state.chat_input = ""  # Reset input value
            process_message(user_input)

        if st.session_state.messages:
            for message in st.session_state.messages:
                if message['role'] == 'user':
                    st.write(f"You: {message['content']}")
                else:
                    st.write(f"Assistant: {message['content']}")
        for msg in st.session_state.messages:
            if msg['role'] == "user":
                st.write(f"You: {msg['content']}")
            else:
                st.write(f"Assistant: {msg['content']}")

        if st.button("Save Conversation"):
            save_conversation()
