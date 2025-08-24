# making role for media converter and attaching the s3 and api gateway 
# this get attached in the lambda 
resource "aws_iam_role" "mediaconvert" {
  name = "MediaConvert_Default_Role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "mediaconvert.amazonaws.com"
        }
      }
    ]
  })
}

# Attach AmazonS3FullAccess
resource "aws_iam_role_policy_attachment" "mediaconvert_s3" {
  role       = aws_iam_role.mediaconvert.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

# Attach AmazonAPIGatewayInvokeFullAccess
resource "aws_iam_role_policy_attachment" "mediaconvert_apigateway" {
  role       = aws_iam_role.mediaconvert.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess"
}
