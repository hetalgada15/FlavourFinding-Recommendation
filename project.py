import streamlit as st
from transformers import AutoTokenizer, AutoModel, DistilBertTokenizer, DistilBertModel
import torch
from openai import OpenAI
from datetime import datetime

# Access the API keys directly from Streamlit secrets
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client
def setup_openai():
    return OpenAI(api_key=OPENAI_API_KEY)

# Initialize the OpenAI client
client = setup_openai()

# Initialize Hugging Face models and tokenizers
recipe_tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
recipe_model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")
restaurant_tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
restaurant_model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Functions for embedding generation
def get_embedding(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

def convert_text_to_embedding(text):
    return get_embedding(text, recipe_tokenizer, recipe_model)

def get_restaurant_embedding(text):
    return get_embedding(text, restaurant_tokenizer, restaurant_model)

# Function to query Pinecone for recipes
def fetch_recipe_metadata(user_query):
    # Placeholder function for Pinecone query logic
    return []

# Function to generate a new recipe using OpenAI
def create_new_recipe(ingredients):
    prompt = f"Create a detailed recipe using the following ingredients: {', '.join(ingredients)}. Provide a name, description, and steps to make it."
    response = client.Completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500
    )
    recipe_text = response.choices[0].text.strip()
    parts = recipe_text.split('\n', 2)
    name = parts[0]
    description = parts[1]
    steps = parts[2] if len(parts) > 2 else ""
    return {'name': name, 'description': description, 'steps': steps}

# Function to query Pinecone for restaurants
def get_restaurant_metadata(description):
    embedding = get_restaurant_embedding(description)
    # Placeholder function for Pinecone query logic
    return []

# Function to filter messages
def is_relevant_message(content):
    food_related_keywords = ['recipe', 'food', 'ingredients', 'cook', 'cuisine', 'dish', 'meal', 'restaurant']
    return any(keyword in content.lower() for keyword in food_related_keywords)

# Function to process chat messages
def process_message(chat_input):
    if chat_input.strip():
        user_message = {"role": "user", "content": chat_input.strip()}
        st.session_state.messages.append(user_message)
        st.session_state.chat_input = ""  # Clear the input field

        if is_relevant_message(chat_input.strip()):
            response = fetch_model_response(st.session_state.messages)
        else:
            response = "This is not a relevant topic. Please ask about recipes or food-related queries."

        assistant_message = {"role": "assistant", "content": response}
        st.session_state.messages.append(assistant_message)

# Function to fetch model response from OpenAI
def fetch_model_response(messages):
    if messages:
        completion = client.Completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return completion.choices[0].text.strip()
    else:
        return "No message to process."

# Function to save conversation to a file
def save_conversation():
    if st.session_state.messages:
        conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
        filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(conversation)
        st.success(f"Conversation saved as {filename}")

# Main function for the Streamlit app
def main():
    st.sidebar.title("Menu")
    menu_option = st.sidebar.selectbox("Select an Option", ["Find Recipes", "Find Restaurants", "Chat"])

    if menu_option == "Find Recipes":
        user_query = st.sidebar.text_input("Search for a recipe:", "")
        if user_query and (user_query != st.session_state.get('last_query', '')):
            st.session_state.last_query = user_query
            ingredients = user_query.split(', ')
            recipes = fetch_recipe_metadata(user_query)
            if recipes:
                st.session_state.recommended_recipes = [recipe for recipe in recipes][:3]
            else:
                st.session_state.recommended_recipes = [create_new_recipe(ingredients) for _ in range(3)]
            
            st.title("Recommended Recipes")
            if st.session_state.get('recommended_recipes'):
                for recipe in st.session_state.recommended_recipes:
                    st.write("**Name:** " + recipe['name'])
                    st.write("**Description:** " + recipe['description'])
                    st.write("**Steps:** " + recipe['steps'])
                    st.markdown("---")
            else:
                st.write("No recommended recipes found.")

    elif menu_option == "Find Restaurants":
        st.title('Restaurant Finder')
        description = st.text_input('Enter a description of the restaurant to find matches:')
        if st.button('Find Restaurants'):
            if description:
                matches = get_restaurant_metadata(description)
                if matches:
                    st.write(f"**Restaurants Matching Description:**")
                    for match in matches:
                        metadata = match.get('metadata', {})
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
                        st.write(f"**Website:** {metadata.get('website', 'N/A')}")
                        st.write("---")
                else:
                    st.write("No restaurants found matching your description.")

    elif menu_option == "Chat":
        if 'messages' not in st.session_state:
            st.session_state.messages = []

        st.title("Chat with the Assistant")
        chat_input = st.text_input("You: ", key="chat_input")
        
        if st.button("Send"):
            process_message(chat_input)
        
        if st.session_state.messages:
            for message in st.session_state.messages:
                if message['role'] == 'user':
                    st.write(f"You: {message['content']}")
                else:
                    st.write(f"Assistant: {message['content']}")
        
        if st.button("Save Conversation"):
            save_conversation()

if __name__ == "__main__":
    main()
