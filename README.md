# AWS RAG Application with CDK Infrastructure

This project implements a Retrieval-Augmented Generation (RAG) application using AWS services, deployed with the AWS Cloud Development Kit (CDK).

## Overview

The application uses:
- AWS Bedrock for LLM capabilities
- ChromaDB for vector storage
- FastAPI for the API layer
- Docker for containerization
- AWS CDK for infrastructure as code

## Prerequisites

- Python 3.11+
- Docker
- AWS CLI configured with appropriate permissions
- AWS CDK v2
- Node.js 14+ (for CDK)

## Environment Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set up Python environment

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure AWS credentials

Create a `.env` file in the project root with your AWS credentials:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_DEFAULT_REGION=us-east-1
```

### 4. Set up CDK (if deploying to AWS)

```bash
# Install CDK globally if not already installed
npm install -g aws-cdk

# Navigate to the CDK directory
cd rag-cdk-infra

# Install CDK dependencies
npm install

# Bootstrap CDK (only needed once per AWS account/region)
cdk bootstrap

# Deploy the CDK stack
cdk deploy
```

## Building and Running Locally

### Build the Docker image

```bash
docker build -t aws_rag_app -f image/Dockerfile .
```

### Run the application locally

```bash
docker run --platform linux/amd64 --rm -it \
    -p 8000:8000 \
    --env-file .env \
    aws_rag_app
```

The API will be available at http://localhost:8000

## Testing AWS Credentials

To verify your AWS credentials are working correctly:

```bash
docker run --platform linux/amd64 --rm -it \
    --env-file .env \
    --entrypoint python \
    aws_rag_app src/test_aws_credentials.py
```

## API Usage

### Submit a query

```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"query_text": "Your question here"}'
```

## Project Structure

```
.
├── image/
│   └── Dockerfile            # Docker configuration
├── rag-cdk-infra/            # CDK infrastructure code
├── src/
│   ├── app_api_handler.py    # FastAPI application
│   ├── rag_app/
│   │   ├── get_chroma_db.py  # ChromaDB setup
│   │   ├── get_embeddings.py # Bedrock embeddings
│   │   └── query_rag.py      # RAG implementation
│   └── test_aws_credentials.py # AWS credentials test
├── .env                      # Environment variables (not in git)
├── .gitignore                # Git ignore file
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Deployment

The application can be deployed to AWS using the CDK infrastructure code in the `rag-cdk-infra` directory.

```bash
cd rag-cdk-infra
cdk deploy
```

This will deploy:
- An ECS Fargate service running the containerized application
- Required IAM roles and policies
- Networking infrastructure
- Any other required AWS resources

## Troubleshooting

### AWS Credentials Issues

If you encounter AWS credential errors:
1. Verify your `.env` file has the correct credentials without spaces or quotes
2. Ensure your AWS user has the necessary permissions for Bedrock and other services
3. Try running the test script to diagnose credential issues

### Docker Issues

If you encounter Docker-related errors:
1. Ensure Docker is running on your machine
2. Try rebuilding the image with `--no-cache` option
3. Check Docker logs for detailed error messages

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

