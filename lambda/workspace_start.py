# Importing the AWS SDK
import boto3
import logging

log = logging.getLogger()
# Creading workspace client object
client = boto3.client("workspaces")

# Description of all running workspace
response = client.describe_workspaces()

def lambda_handler(event, context):

    # Looping over all workspaces in response
    for workspace in response["Workspaces"]:

        # Some temporary variables for each workspace
        state = str(workspace["State"])
        username = str(workspace["UserName"])
        workspaceId = str(workspace["WorkspaceId"])
        runningMode = workspace["WorkspaceProperties"]["RunningMode"]
        response_tags = client.describe_tags(ResourceId=workspaceId)
        
        if response_tags["TagList"] == [{"Key": "nightly", "Value": "onoff"}]:
            log.info(f"{workspaceId} has the relevent tags")
            # Starting turned off workspaces
            if state == "STOPPED":

                # Starting workspace with the id stored in varibale workspaceId
                client.start_workspaces(
                    StartWorkspaceRequests=[{"WorkspaceId": workspaceId}]
                )