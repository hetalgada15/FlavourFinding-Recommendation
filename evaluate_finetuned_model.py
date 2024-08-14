from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.metrics import FaithfulnessMetric
from deepeval.metrics import ContextualPrecisionMetric
from deepeval.metrics import ContextualRecallMetric
from deepeval.metrics import ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase
import pandas as pd
import os

# Set the OpenAI API key directly in the script
os.environ["OPENAI_API_KEY"] = "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"

# Load the Excel file
df = pd.read_excel("updated_recipes_evaluation.xlsx")

# Define enhanced metrics
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
    threshold=0.7,  # Experiment with different thresholds
    model="gpt-4o-mini",
    include_reason=True
)
ContextualRelevancy = ContextualRelevancyMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

metrics = [AnswerRelevancy, ContextualPrecision, ContextualRelevancy, ContextualRecall, Faithfulness]

# Create test cases from the DataFrame
test_cases = []
for index, row in df.iterrows():
    test_case = LLMTestCase(
        input=row["Query"],
        actual_output=row["Actual Output"],
        expected_output=row["Expected Output"],
        retrieval_context=[row["Retrieval Context"]]
    )
    test_cases.append(test_case)

# Evaluate the test cases using the defined metrics
results = evaluate(test_cases, metrics)

# Print results for analysis
print("Evaluation Results:", results)
