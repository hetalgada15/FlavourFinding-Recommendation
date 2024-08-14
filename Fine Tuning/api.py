# import openai
# import streamlit as st
# import json
# import logging
# import os

# # Set up logging to capture process details
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Load the smaller training data
# with open('fine_tuning_data_small.json', 'r') as f:
#     training_data = json.load(f)

# # Function to run a prompt-based customization using gpt-3.5-turbo
# def run_custom_prompt(training_data, chat_history):
#     try:
#         openai.api_key = st.secrets["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"]  # Ensure you have your OpenAI API key in Streamlit secrets

#         for example in training_data:
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": example['input']},
#                     {"role": "assistant", "content": example['output']}
#                 ],
#                 temperature=0.7,
#                 max_tokens=150
#             )

#             # Add user and assistant messages to chat history
#             chat_history.append({"role": "user", "content": example['input']})
#             chat_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

#             # Log the chat
#             logging.info(f"User Prompt: {example['input']}")
#             logging.info(f"Model Response: {response['choices'][0]['message']['content']}")
#             logging.info("-" * 50)

#     except Exception as e:
#         logging.error(f"An error occurred: {str(e)}")

# # Function to save chat history to a file
# def save_chat_history(chat_history):
#     with open("chat_history.json", "w") as f:
#         json.dump(chat_history, f, indent=4)
#     st.success("Chat history saved!")

# # Initialize the chat history
# if "chat_history" not in st.session_state:
#     st.session_state["chat_history"] = []

# # Title of the Streamlit app
# st.title("Chatbot with Fine-Tuning")

# # Display the chat history
# if st.session_state["chat_history"]:
#     for chat in st.session_state["chat_history"]:
#         if chat["role"] == "user":
#             st.write(f"**You:** {chat['content']}")
#         else:
#             st.write(f"**Bot:** {chat['content']}")

# # Text input for user to enter their query
# user_input = st.text_input("You:", "")

# # If the user provides an input
# if user_input:
#     st.session_state["chat_history"].append({"role": "user", "content": user_input})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=st.session_state["chat_history"],
#         temperature=0.7,
#         max_tokens=150
#     )
#     st.session_state["chat_history"].append({"role": "assistant", "content": response['choices'][0]['message']['content']})

# # Display buttons for saving chat history and starting a new conversation
# if st.button("Save Chat History"):
#     save_chat_history(st.session_state["chat_history"])

# if st.button("Start New Conversation"):
#     st.session_state["chat_history"] = []

# # Run the custom prompt-based approach
# run_custom_prompt(training_data, st.session_state["chat_history"])

import openai
import streamlit as st
import json
import logging

# Set up logging to capture process details
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace this with your actual OpenAI API key
openai.api_key = "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"

# Function to run a prompt-based customization using gpt-3.5-turbo
def run_custom_prompt(user_input, chat_history):
    try:
        # Append the user message to chat history
        chat_history.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            temperature=0.7,
            max_tokens=150
        )

        # Append the assistant's response to chat history
        chat_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

        # Return the assistant's response
        return response['choices'][0]['message']['content']

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return None

# Function to save chat history to a file
def save_chat_history(chat_history):
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=4)
    st.success("Chat history saved!")

# Initialize the chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Title of the Streamlit app
st.title("Chatbot with Fine-Tuning")

# Display the chat history
if st.session_state["chat_history"]:
    for chat in st.session_state["chat_history"]:
        if chat["role"] == "user":
            st.write(f"**You:** {chat['content']}")
        else:
            st.write(f"**Bot:** {chat['content']}")

# Text input for user to enter their query
user_input = st.text_input("Enter your message:", "")

# Buttons for interaction
enter_button = st.button("Enter")
save_button = st.button("Save History")
clear_button = st.button("Clear Conversation")

# Handle the Enter button
if enter_button and user_input:
    response = run_custom_prompt(user_input, st.session_state["chat_history"])
    if response:
        st.session_state["chat_history"].append({"role": "assistant", "content": response})
    # Instead of rerunning, display the response immediately
    st.write(f"**You:** {user_input}")
    st.write(f"**Bot:** {response}")

# Handle the Save History button
if save_button:
    save_chat_history(st.session_state["chat_history"])

# Handle the Clear Conversation button
if clear_button:
    st.session_state["chat_history"] = []
    st.experimental_set_query_params()  # This reloads the page and clears the session state

