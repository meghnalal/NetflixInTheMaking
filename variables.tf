variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-2"
}
# defining the name in here for the buckets
variable "input_video_netflix" {
  description = "Name of the input S3 bucket"
  type        = string
  default     = "inputvideonetflix"
}

variable "output_video_netflix" {
  description = "Name of the output S3 bucket"
  type        = string
  default     = "outputvideonetflix"
}
