from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

# Initialize Mira Client with API Key
client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})

# Load the medical assistance AI flow configuration
flow = CompoundFlow(source="flow.yaml")

# Prepare test inputs
test_input = {
    "symptoms": "Fever, headache, sore throat",  # Example symptoms
    "location": "San Francisco, CA"             # Example location
}

try:
    # Test the compound flow with the inputs
    response = client.flow.test(flow, test_input)
    print("Test response:", response)  # Output the test results
except FlowError as e:
    print("Test failed:", str(e))      # Handle any errors during testing
