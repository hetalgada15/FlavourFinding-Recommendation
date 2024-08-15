# Recipe Recommendation System Evaluation with DeepEval

## Overview

This project is designed to evaluate a Retrieval-Augmented Generation (RAG) chatbot focused on recipe recommendation using the DeepEval library. The evaluation emphasizes key metrics such as Answer Relevancy, Faithfulness, Contextual Precision, Contextual Recall, and Contextual Relevancy, which are critical for assessing the quality of recipe recommendations provided by the chatbot.

The evaluation process uses an Excel document containing test cases that simulate real-world recipe queries and their expected outputs.

We utilize `gpt-4o-mini` for the evaluation, so please ensure your `OPENAI_API_KEY` is correctly configured in your `.env` file.

## Metrics

### 1. Answer Relevancy

The Answer Relevancy metric measures the quality of your recipe recommendation system by evaluating how relevant the actual output (recommended recipes) is compared to the user’s query. This metric is self-explaining, meaning it provides a reason for the relevancy score it generates. The score is calculated as follows:


- **Number of Relevant Recipes**: The count of recipes in the chatbot's response that are considered relevant to the ingredients or type of dish specified in the user’s query.
- **Total Number of Recipes**: The total count of recipes recommended by the chatbot.

### 2. Faithfulness

The Faithfulness metric assesses whether the recommended recipes factually align with the retrieved content. This ensures that the recipes suggested by the chatbot are based on accurate information from the database or knowledge base. Like the other metrics, it is self-explaining and provides a rationale for its score.


- **Number of Truthful Claims**: The count of claims in the recipe (e.g., ingredient lists, cooking methods) that are factually correct and align with the retrieved recipe data.
- **Total Number of Claims**: The total count of claims made in the recommended recipes.

### 3. Contextual Precision

The Contextual Precision metric evaluates whether the most relevant recipe components (e.g., key ingredients, cooking techniques) are prioritized in the retrieval context. This ensures that the chatbot’s recipe suggestions emphasize the most important aspects of the user’s query.


### 4. Contextual Recall

The Contextual Recall metric measures the extent to which the retrieval context includes all necessary information relevant to the user’s query. This ensures that the chatbot captures all the relevant details (e.g., all specified ingredients or dietary requirements) when suggesting recipes.


### 5. Contextual Relevancy

The Contextual Relevancy metric assesses the overall relevance of the recipes suggested by the chatbot in relation to the user's input. This metric is crucial for ensuring that the recipes are not only accurate but also aligned with the user’s preferences or requirements.

## Getting Started

These instructions will guide you through the setup and evaluation process.

### Prerequisites

- Python 3.x
- Pandas
- DeepEval library

You can install the required libraries using pip:

```bash
pip install deepeval
```

### Setup

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/Recipe-Recommendation-Evaluation.git
   cd Recipe-Recommendation-Evaluation
   ```

2. **Set up your environment**:
   - Ensure your chatbot's output data and the corresponding input data are available in a suitable format (e.g., Excel, CSV, JSON).
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

### Running the Evaluation

1. **Load your chatbot's output data** into a pandas DataFrame.
2. **Use DeepEval** to calculate the relevant metric scores for each recipe recommendation response:
   - Metrics: Answer Relevancy, Faithfulness, Contextual Precision, Contextual Recall, Contextual Relevancy.
3. **Analyze the results** to understand the performance of your recipe recommendation system.

## Methods to Improve Metrics

### Improving Answer Relevancy

- **Enhance the Retrieval Mechanism**: Improve the quality of retrieved recipes by fine-tuning the retrieval algorithm. This could involve optimizing the ranking model to prioritize recipes that better match the user’s query.
- **Contextual Embeddings**: Utilize advanced contextual embeddings like BERT or GPT to better understand the ingredients or dish type specified in the user’s query and generate more relevant recipe recommendations.
- **Response Filtering**: Implement a filtering mechanism to remove irrelevant or low-quality recipes before presenting the final recommendations to the user.

### Improving Faithfulness

- **Fact-Checking Module**: Integrate a fact-checking module that verifies the accuracy of the recommended recipes against the retrieved recipe data before finalizing the suggestions.
- **Knowledge Base Integration**: Enhance the recipe recommendation system by integrating it with a reliable and up-to-date recipe database to cross-verify the facts mentioned in the recommendations.
- **Training with Factually Correct Data**: Fine-tune the generator model on datasets that emphasize recipe accuracy to improve its ability to generate truthful and reliable recipes.

## Documentation and Analysis

- **Document Changes**: Keep a detailed record of all modifications made to the recipe recommendation system, including changes to algorithms, models, and integration of new modules.
- **Performance Analysis**: After implementing the proposed methods, analyze their impact on the overall performance of the recipe recommendation system. This includes measuring improvements in the Answer Relevancy and Faithfulness metrics and comparing them with baseline performance.
- **Iterative Refinement**: Based on the analysis, continuously refine and optimize the methods to achieve better performance.

---
