FROM public.ecr.aws/lambda/python:3.11

# Copy source code
COPY src ${LAMBDA_TASK_ROOT}/src

# Copy test script
COPY src/test_aws_credentials.py ${LAMBDA_TASK_ROOT}/src/

# Copy requirements.txt and pyproject.toml
COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY pyproject.toml ${LAMBDA_TASK_ROOT}

# Install build dependencies and your package's dependencies
RUN pip install --upgrade pip && \
    pip install build

# Required to make SQLlite3 work for Chroma.
RUN pip install pysqlite3-binary

# Install the specified packages
RUN pip install -r requirements.txt --upgrade

# Add the src directory to Python path
ENV PYTHONPATH="${LAMBDA_TASK_ROOT}"

# For local testing.
EXPOSE 8000

# Set IS_USING_IMAGE_RUNTIME Environment Variable
ENV IS_USING_IMAGE_RUNTIME=True

# Copy data directory if it exists
COPY src/data/chroma ${LAMBDA_TASK_ROOT}/data/chroma

# Set default AWS region
ENV AWS_DEFAULT_REGION=us-east-1
