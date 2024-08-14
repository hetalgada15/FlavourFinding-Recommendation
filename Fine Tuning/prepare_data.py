import pandas as pd
import json
import time

# Load the datasets
restaurants_df = pd.read_csv('cleaned_restaurants.csv')
recipes_df = pd.read_csv('cleaned_food_recipe.csv')

start_time = time.time()

# Define a function to create the training examples
def create_training_examples(row):
    examples = []
    for _, recipe in recipes_df.iterrows():
        input_text = (
            f"Recommend a restaurant for {recipe['name']} "
            f"in {row['city']}, {row['state']}. "
            f"It should serve {row['description']}."
        )
        output_text = (
            f"I recommend {row['name']} located at {row['displayAddress']}. "
            f"It is known for {row['description']}, "
            f"with an average rating of {row['averageRating']} stars."
        )
        examples.append({"input": input_text, "output": output_text})
    return examples

# Apply the function to each row in the restaurants dataframe
all_examples = restaurants_df.apply(lambda row: create_training_examples(row), axis=1)

# Flatten the list of lists
training_data = [example for sublist in all_examples for example in sublist]

# Save the data as a JSON file
with open('fine_tuning_data.json', 'w') as f:
    json.dump(training_data, f, indent=4)

print("Training data preparation complete.")
print(f"Processing took {time.time() - start_time} seconds.")
