import openai
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ContextualPrecisionMetric, ContextualRecallMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase
import streamlit as st


# Set up your OpenAI API key
# Access the API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Generate the response using the fine-tuned model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use your fine-tuned model's name if it's different
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Recommend a restaurant in Houston, TX that serves American burgers and offers a dish similar to Zesty Spaghetti Aglio E Olio with Lemon and Spinach."}
    ],
    temperature=0.7,
    max_tokens=150
)

# Extract the model's response
model_output = response['choices'][0]['message']['content']

# Define the test case
test_case = LLMTestCase(
    input="Recommend a restaurant in Houston, TX that serves American burgers and offers a dish similar to Zesty Spaghetti Aglio E Olio with Lemon and Spinach.",
    actual_output=model_output,
    expected_output="I recommend mcdonald's located at 2017 main st parking, 2017 main st, houston, tx 77002, usa. It is known for american, burgers, with an average rating of 3.850296021 stars."
)

# Define metrics
metrics = [
    AnswerRelevancyMetric(threshold=0.7, model="gpt-4o-mini", include_reason=True),
    FaithfulnessMetric(threshold=0.7, model="gpt-4o-mini", include_reason=True),
    ContextualPrecisionMetric(threshold=0.7, model="gpt-4o-mini", include_reason=True),
    ContextualRecallMetric(threshold=0.7, model="gpt-4o-mini", include_reason=True),
    ContextualRelevancyMetric(threshold=0.7, model="gpt-4o-mini", include_reason=True)
]

# Evaluate the test case
evaluation_results = evaluate([test_case], metrics)

# Print evaluation results
for metric, result in zip(metrics, evaluation_results):
    print(f"{metric.__class__.__name__}: {result['score']}")
    print(f"Reason: {result['reason']}")
