import boto3
import os
import logging
import json
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv(verbose=True)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_aws_credentials():
    # Print environment variables (without sensitive values)
    print("AWS_DEFAULT_REGION:", os.environ.get("AWS_DEFAULT_REGION"))
    print("AWS_ACCESS_KEY_ID exists:", bool(os.environ.get("AWS_ACCESS_KEY_ID")))
    print("AWS_SECRET_ACCESS_KEY exists:", bool(os.environ.get("AWS_SECRET_ACCESS_KEY")))
    return "Verified AWS Credentials"      
    
    



def list_foundation_models(bedrock_client):
    """
    Gets a list of available Amazon Bedrock foundation models.

    :return: The list of available bedrock foundation models.
    """

    try:
        response = bedrock_client.list_foundation_models()
        models = response["modelSummaries"]
        logger.info("Got %s foundation models.", len(models))
        return models

    except ClientError:
        logger.error("Couldn't list foundation models.")
        raise


def main():
    """Entry point for the example. Uses the AWS SDK for Python (Boto3)
    to create an Amazon Bedrock client. Then lists the available Bedrock models
    in the region set in the callers profile and credentials.
    """

    bedrock_client = boto3.client(service_name="bedrock", region_name="us-east-1",
                                  aws_access_key_id= os.environ.get("AWS_SECRET_ACCESS_KEY"),
                                  aws_secret_access_key= os.environ.get("AWS_SECRET_ACCESS_KEY"))

    fm_models = list_foundation_models(bedrock_client)
    for model in fm_models:
        print(f"Model: {model['modelName']}")
        print(json.dumps(model, indent=2))
        print("---------------------------\n")

    logger.info("Done.")


if __name__ == "__main__":
    test_aws_credentials()
    main()