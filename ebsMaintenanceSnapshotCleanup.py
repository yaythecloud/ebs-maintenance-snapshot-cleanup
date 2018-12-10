import boto3
import datetime
import json

def lambda_handler(event, context):
    
    c = boto3.client('ec2')
    
    # print script is starting to cloudwatch logs
    print("---function starting: Clean up maintenance snapshots---")
    
    # function to retrieve all snapshots with the tag values [Name: Maintenance, Value: True]
    snapshots = c.describe_snapshots(
        Filters=[
            {
                'Name': "tag:Maintenance",
                'Values': [
                    "True"
                ]
            },
        ]
    )
    print("---the following snapshots were found with key value pair [maintenance:true]---")
    print(snapshots)
    
    snaps = snapshots['Snapshots']
    print(snaps)
    
    # for loop to obtain all snapshots with the maintenance:true key value pair and delete them
    for snap_id in snaps:
        print(snap_id)
        # print the snap_id
        print(snap_id['SnapshotId'])
        snap_id = c.delete_snapshot(
            SnapshotId = snap_id['SnapshotId']
        )
    print("---snapshots removed---")