
import openai
openai.api_key = "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"



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
evaluate(test_cases, metrics)
