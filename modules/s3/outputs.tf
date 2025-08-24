output "input_bucket_id" {
  value = aws_s3_bucket.input.id
}

output "input_bucket_arn" {
  value = aws_s3_bucket.input.arn
}

output "output_bucket_id" {
  value = aws_s3_bucket.output.id
}

output "output_bucket_arn" {
  value = aws_s3_bucket.output.arn
}

output "output_bucket_domain_name" {
  value = aws_s3_bucket.output.bucket_regional_domain_name
}