provider "aws" {
  region = "us-west-2"
}

resource "aws_lambda_function" "rag_lambda" {
  function_name = "RAGPipelineLambda"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  # Assuming your module is uploaded to S3 as a zip
  s3_bucket        = "your-bucket-name"
  s3_key           = "path-to-your-package/rag_pipeline.zip"

  environment {
    variables = {
      VECTOR_DB_DIR = "path/to/chroma_db"
    }
  }
}

resource "aws_iam_role" "lambda_exec" {
  name = "rag_lambda_exec_role"

  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
