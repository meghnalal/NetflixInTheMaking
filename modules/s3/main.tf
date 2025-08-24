resource "aws_s3_bucket" "input" {
  bucket = var.input_bucket_name
}
resource "aws_s3_bucket" "output" {
  bucket = var.output_bucket_name
}

# I need the bucket to allow CloudFront 
# hence why it got passed as variable from main so It can add these permission
resource "aws_s3_bucket_policy" "output_bucket_policy" {
  bucket = aws_s3_bucket.output.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "cloudfront.amazonaws.com"
        }
        Action   = "s3:GetObject"
        Resource = "${aws_s3_bucket.output.arn}/*"
        Condition = {
          StringEquals = {
            "AWS:SourceArn" = var.cloudfront_arn
          }
        }
      }
    ]
  })
}
