import boto3
from langchain_aws import BedrockEmbeddings
import os

def get_embedding_function():
    # Clean up any potential spaces in the region name
    region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1").strip()
    
    # Create a boto3 session with explicit credentials
    session = boto3.Session(region_name=region, aws_access_key_id='',
                                  aws_secret_access_key='')
    
    embeddings = BedrockEmbeddings(
        client=session.client("bedrock-runtime"),
        model_id="amazon.titan-embed-text-v1"
    )
    return embeddings
