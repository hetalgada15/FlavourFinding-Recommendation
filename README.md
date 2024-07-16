# FlavourFinding-Recommendation

An intelligent application designed to classify and respond to user queries about recipes, ingredients, and restaurants using NLP techniques and three distinct datasets. It features efficient data retrieval and a user-friendly interface for seamless interaction.

## Objectives and Goals

- **Accurate Query Classification:** Implement an NLP-based system to classify user queries into categories such as recipes, ingredients, or restaurants.
- **Efficient Data Retrieval:** Develop modules to handle queries for each dataset independently, ensuring fast and accurate data retrieval.
- **User-Friendly Interface:** Create an intuitive interface that allows users to input natural language queries and receive relevant information quickly.
- **Scalability and Reliability:** Ensure the system is scalable and reliable, capable of handling multiple user queries simultaneously.

## Project Architecture

The project is structured into three main components:

1. **Data Preprocessing and Management:**
   - **Preprocess:** Clean and normalize each dataset to ensure data quality.
   - **Manage:** Load datasets into efficient data structures for fast querying.

2. **Query Handling and NLP:**
   - **Classify Queries:** Use NLP techniques to classify user queries into relevant categories.
   - **Route Queries:** Route the classified queries to the appropriate dataset module.

3. **Individual Dataset Query Systems and User Interface:**
   - **Restaurant Query Module:** Handle queries related to restaurants.
   - **Recipe Query Module:** Handle queries related to recipes.
   - **User Interface:** Develop a user-friendly interface for seamless interaction.

## Datasets

1. **Recipes Dataset:** Contains information about various recipes, including ingredients, steps, and cooking methods.
2. **Ingredients Dataset:** Provides details about different food ingredients, including nutritional information, categories, and common uses.
3. **Restaurants Dataset:** Includes information about restaurants, such as location, menu items, and reviews.

## Implementation Plan

### Data Preprocessing and Management

- Clean and normalize the recipes, ingredients, and restaurants datasets.
- Ensure consistency in naming conventions and handle missing values.
- Load datasets into efficient data structures to support fast querying.

### Query Handling and NLP

- Develop an NLP model to classify user queries into categories (e.g., recipe-related, restaurant-related).
- Use keyword matching, intent recognition, and context analysis for accurate classification.
- Route classified queries to the appropriate dataset module.

### Individual Dataset Query Systems and User Interface

- Implement functions to query the recipes and restaurants datasets based on various attributes.
- Design and develop a user-friendly interface for natural language input and retrieval.

