import json
import boto3

glueClient = boto3.client("glue")

def lambda_handler(event, context):
    # TODO implement
    glueClient.start_job_run(JobName="csvtojson")
    return "Job started"
