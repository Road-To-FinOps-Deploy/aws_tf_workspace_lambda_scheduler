# Importing the aws SDK
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
        RunningMode = workspace["WorkspaceProperties"]["RunningMode"]
        workspaceId = str(workspace["WorkspaceId"])
        response_tags = client.describe_tags(ResourceId=workspaceId)
        if response_tags["TagList"] == [{"Key": "nightly", "Value": "onoff"}]:
            # Checking if the running mode is Auto Stop
            log.info(f"{workspaceId} has the relevent tags")
            if RunningMode == "AUTO_STOP":
                # Making the auto stop timeout 60 minutes
                try:
                    client.modify_workspace_properties(
                        WorkspaceId=workspaceId,
                        WorkspaceProperties={"RunningModeAutoStopTimeoutInMinutes": 60},
                    )
                    print(f"{workspaceId} modified")
                except:
                    log.warning(f"Unexpected error" )
