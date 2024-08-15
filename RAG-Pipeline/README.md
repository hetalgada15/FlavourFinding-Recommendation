# FlavorFinder - A Smart Food Data Retrieval and Recommendation System

[RAG-Pipeline Video](https://youtu.be/SeEZs1P1Cm8)

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Dependencies](#dependencies)
- [Usage Guidelines](#usage-guidelines)
  - [1. Find Recipes](#1-find-recipes)
  - [2. Find Restaurants](#2-find-restaurants)
  - [3. Chat with the Assistant](#3-chat-with-the-assistant)
  - [4. Save Conversations](#4-save-conversations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

**FlavourFinding** is an innovative system designed to enhance the culinary experience by providing personalized recipe recommendations and restaurant suggestions. Leveraging cutting-edge technologies such as Pinecone, OpenAI, and Transformers, this system allows users to interact with an AI-powered assistant to discover recipes and restaurants tailored to their tastes and preferences.

Whether you're a food enthusiast, a professional chef, or simply someone looking to try something new, FlavourFinding is here to help you explore and find the perfect dish or dining experience.

## Architecture Diagram

![image](https://github.com/user-attachments/assets/4406e735-59a3-4cf2-b8e9-e6391aa31f01)

### Detailed Architecture Explanation

1. **Document Loaders**: This component handles the ingestion of various food-related documents, which could include recipes, restaurant menus, or other culinary data.

2. **Data Preprocessing**: The loaded documents are segmented into smaller, more manageable chunks. These chunks are summarized, and embeddings are generated using a pre-trained Large Language Model (LLM). This step ensures that the data is efficiently searchable within the vector database.

3. **Vector Database**: The preprocessed data chunks are stored as vector embeddings in a Pinecone-powered vector database. This allows for rapid similarity searches, enabling the system to find relevant information quickly and accurately.

4. **Self-Querying with LLM**: When a user submits a query, the system generates an embedding for the query using the LLM. This embedding is then used to search the vector database for matching documents.

5. **Hybrid Querying**: The system uses a combination of traditional search techniques and AI-based querying methods, including Hybrid Dense Embeddings (HyDE), to enhance the accuracy and relevance of search results.

6. **Retriever**: The retriever component fetches the most relevant documents or data chunks from the vector database based on the generated query embeddings.

7. **Answer Generation**: The system uses the LLM to generate a detailed answer based on the retrieved documents. This answer generation process may involve re-ranking documents, summarizing content, and applying map-reduce techniques to produce a coherent and useful response.

8. **User Interaction**: The final response is delivered to the user through a user-friendly interface, where they can ask follow-up questions or explore additional queries.

## Setup Instructions
(project.py is located outside of this folder)

### Prerequisites

- Python 3.7 or higher
- Git
- An IDE or text editor of your choice (e.g., VSCode, PyCharm)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/hetalgada15/FlavourFinding-Recommendation.git
    cd FlavourFinding-Recommendation
    ```

2. **Create and Activate a Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys**:
    - Create a `.streamlit/secrets.toml` file in the root of the project with the following content:
      ```toml
      PINECONE_API_KEY = "your-pinecone-api-key"
      OPENAI_API_KEY = "your-openai-api-key"
      ```

### Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run project.py
```

## Dependencies

- **Streamlit**: A web framework for creating interactive data applications.
- **Transformers**: NLP models library from Hugging Face, used here for generating embeddings.
- **Pinecone**: A vector database enabling fast and scalable similarity searches.
- **OpenAI API**: Provides GPT-3.5-Turbo for generating responses and content.
- **PyTorch**: A deep learning library used by the Transformers models for generating embeddings.

## Usage Guidelines

### 1. Find Recipes

- Navigate to the "Find Recipes" section in the sidebar.
- Enter a list of ingredients or a specific recipe query.
- The system will search the database for matching recipes. If no matches are found, it will generate new recipes using the OpenAI API.

### 2. Find Restaurants

- Navigate to the "Find Restaurants" section.
- Enter a description of the restaurant you’re looking for.
- The system will return a list of matching restaurants based on your input.

### 3. Chat with the Assistant

- Go to the "Chat" section.
- Ask any food-related questions or provide queries, and the assistant will respond with relevant information.

### 4. Save Conversations

- Use the "Save Conversation" button to save your chat history as a text file. The file will be named with a timestamp for easy reference.

## Future Enhancements

**Potential Extensions:**
 - Integration with smart kitchen devices for real-time recipe adjustments.
 - Features like meal planning and automatic grocery list generation.

**Long-term Vision:**
 - Develop a comprehensive culinary assistant that o>ers AI-driven enhancements for both 
home cooks and food enthusiasts.

**Further Development:**
 - Collaborate with chefs and food platforms to expand the recipe database and enhance 
the recommendation engine


## Collaborators & Contributions

Collaborators: 
- Hetal Gada: gada.he@northeastern.edu
- Dristi Dani: dani.d@northeastern.edu
- Vishwa Shah: shah.vishw@northeastern.edu

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/hetalgada15/FlavourFinding-Recommendation/blob/main/LICENSE) file for details.

---
