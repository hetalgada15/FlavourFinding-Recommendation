import openai
import json
import logging

# Set up logging to capture process details
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the smaller training data
with open('fine_tuning_data_small.json', 'r') as f:
    training_data = json.load(f)

# Function to run a prompt-based customization using gpt-3.5-turbo
def run_custom_prompt(training_data):
    try:
        openai.api_key = "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"  # Replace with your actual OpenAI API key

        # Iterate through your custom training data
        for example in training_data:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that also adds a hint of sarcasm."},
                    {"role": "user", "content": example['input']},
                    {"role": "assistant", "content": example['output']}
                ],
                temperature=0.7,
                max_tokens=150
            )

            logging.info(f"User Prompt: {example['input']}")
            logging.info(f"Expected Response: {example['output']}")
            logging.info(f"Model Response: {response['choices'][0]['message']['content']}")
            logging.info("-" * 50)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Run the custom prompt-based approach
run_custom_prompt(training_data)
