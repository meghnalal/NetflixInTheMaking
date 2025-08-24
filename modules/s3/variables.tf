variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-2"
}

# defining that bucket_names should be strings 
variable "input_bucket_name" {
  type = string
}

variable "output_bucket_name" {
  type = string
}

variable "cloudfront_arn" {
  type = string
}
