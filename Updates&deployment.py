from mira_sdk import MiraClient, Flow, CompoundFlow
from mira_sdk.exceptions import FlowError

# Initialize MiraClient
client = MiraClient()

# Retrieve existing flow
flow = client.flow.get("shivam/medical-assistance-ai-flow")  # Replace with your username and flow name

# Save the flow locally for editing
flow.save("/path/to/medical_assistance_ai_flow.yaml")  # Update with your desired path

try:
    # Deploy the updated version of the flow
    client.flow.deploy(flow)
    print("Updated flow deployed successfully!")  # Success message

except FlowError as e:
    # Handle update error
    print(f"Update error: {str(e)}")

# In case you forget to bump the flow version, it will get bumped by default every time you deploy the same flow.
