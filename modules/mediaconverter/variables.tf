# ==========================
# Variables you should define in variables.tf
# ==========================
variable "s3_bucket_id" {}
variable "s3_bucket_arn" {}
variable "lambda_name" { default = "lambda_exec_media_converter" }
variable "lambda_role_name" { default = "lambda_role_media_converter" }
variable "lambda_handler" { default = "lambda_function.lambda_handler" }
variable "lambda_runtime" { default = "python3.9" }
variable "lambda_zip_file" { default = "lambda_function_payload.zip" }
