import openai
import streamlit as st
from deepeval import evaluate
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric
)
from deepeval.test_case import LLMTestCase
import pandas as pd

# Access the API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Load the Excel file
df = pd.read_excel("updated_recipes_evaluation.xlsx")

# Define metrics
AnswerRelevancy = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

Faithfulness = FaithfulnessMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

ContextualPrecision = ContextualPrecisionMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

ContextualRecall = ContextualRecallMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

ContextualRelevancy = ContextualRelevancyMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

metrics = [
    AnswerRelevancy,
    ContextualPrecision,
    ContextualRelevancy,
    ContextualRecall,
    Faithfulness
]

test_cases = []
for index, row in df.iterrows():
    test_case = LLMTestCase(
        input=row["Query"],
        actual_output=row["Actual Output"],
        expected_output=row["Expected Output"],
        retrieval_context=[row["Retrieval Context"]]
    )
    test_cases.append(test_case)

# Evaluate test cases
results = evaluate(test_cases, metrics)

# Print or process the results
for result in results:
    print(result)
