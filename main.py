from workflows.startup import StartupWorkflow
from workflows.saas import SaaSWorkflow

idea = input("Describe your startup:\n")

mode = input(
    "Mode(startup/saas): "
)

if mode == "saas":

    workflow = SaaSWorkflow()

else:

    workflow = StartupWorkflow()

result = workflow.run(idea)

print("Project generated successfully.")
