# Fine-Tuned Model for Restaurant and Recipe Recommendations

[Fine Tuning Model Video](https://youtu.be/t06grMWrOJY)

## Overview

This project involves fine-tuning a GPT-3.5-turbo model to improve its performance in recommending restaurants based on specific dishes or cuisines. The fine-tuning process utilizes custom training data generated from a combination of restaurant and recipe datasets. The model is then evaluated using a set of predefined metrics to assess its performance.

## Project Structure

```bash
├── evaluate_finetuned_model.py   # Script to evaluate the fine-tuned model using custom metrics.
├── fine_tune_model_small.py      # Script to run prompt-based customization using a smaller subset of training data.
├── prepare_data.py               # Script to prepare and generate fine-tuning data from raw datasets.
├── fine_tuning_data.json         # The final JSON file containing training data for fine-tuning the model.
├── fine_tuning_data_small.json   # A smaller subset of the training data for testing or smaller scale fine-tuning.
├── cleaned_restaurants.csv       # CSV file containing cleaned restaurant data.
├── cleaned_food_recipe.csv       # CSV file containing cleaned recipe data.
```

## Workflow

### 1. Data Preparation (`prepare_data.py`)

The data preparation script processes restaurant and recipe datasets to generate custom input-output pairs that will be used for fine-tuning the model.

- **Input**: Restaurant and recipe data.
- **Output**: A JSON file (`fine_tuning_data.json`) containing training examples where the model is prompted to recommend restaurants based on specific dishes.

**Key Steps**:
- Load restaurant and recipe datasets.
- Generate input-output pairs where the input is a prompt requesting a restaurant recommendation and the output is a detailed recommendation.
- Save the generated examples to a JSON file for use in fine-tuning.

### 2. Fine-Tuning the Model (`fine_tune_model_small.py`)

This script utilizes the generated training data to fine-tune the GPT-3.5-turbo model. The fine-tuning process is applied to a smaller dataset for quicker testing and validation.

- **Model**: GPT-3.5-turbo
- **Training Data**: A smaller subset of the generated training data (`fine_tuning_data_small.json`).

**Key Steps**:
- Load the smaller training dataset.
- Use the OpenAI API to run prompt-based fine-tuning, incorporating custom behaviors like adding sarcasm to the assistant’s responses.
- Log the process details, including user prompts, expected responses, and actual model outputs.

### 3. Model Evaluation (`evaluate_finetuned_model.py`)

After fine-tuning, the model is evaluated using several custom metrics to determine its performance.

- **Metrics**: 
  - **Answer Relevancy**: Measures how relevant the model’s output is to the user’s query.
  - **Faithfulness**: Assesses whether the model’s output aligns factually with the provided context.
  - **Contextual Precision**: Evaluates if the most relevant aspects of the context are emphasized.
  - **Contextual Recall**: Checks if the model’s response includes all necessary details from the context.
  - **Contextual Relevancy**: Assesses the overall relevance of the response to the input query.

**Key Steps**:
- Set up the OpenAI API key.
- Generate a response using the fine-tuned model.
- Define a test case that compares the model's output against the expected output.
- Evaluate the test case using the specified metrics.
- Output the results, including the score and reason for each metric.

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key
- Required Python libraries (listed in `requirements.txt` or can be installed via pip)

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hetalgada15/FlavourFinding-Recommendation.git
   cd FlavourFinding-Recommendation/Fine\ Tuning
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Training Data**:
   - Run `prepare_data.py` to generate the fine-tuning data.

4. **Fine-Tune the Model**:
   - Use `fine_tune_model_small.py` to fine-tune the model on the smaller dataset.

5. **Evaluate the Fine-Tuned Model**:
   - Run `evaluate_finetuned_model.py` to assess the performance of your fine-tuned model.

## Usage

- **Data Preparation**: Customize the `prepare_data.py` script if you need to adjust the data generation process.
- **Fine-Tuning**: Modify `fine_tune_model_small.py` for different model behaviors or fine-tuning strategies.
- **Evaluation**: Adjust the evaluation criteria in `evaluate_finetuned_model.py` to focus on different performance aspects.

## Future Work

- **Expand the Training Data**: Use the full dataset for a more comprehensive fine-tuning process.
- **Explore Different Models**: Experiment with other models like GPT-4 or other fine-tuned versions.
- **Optimize Metrics**: Refine the custom metrics or add new ones to further evaluate specific aspects of the model’s performance.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
