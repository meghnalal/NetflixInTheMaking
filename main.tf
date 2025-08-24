# passing to module with bucket name defined in var
# passing clould front arn as its needed for policy
module "s3" {
  source             = "./modules/s3"
  region             = var.region
  input_bucket_name  = var.input_video_netflix
  output_bucket_name = var.output_video_netflix
  cloudfront_arn     = module.cloudfront.distribution_arn
}

module "iam" {
  source = "./modules/iam"
}

# passing to module with bucket id and arn as i need it to trigger for lambda
module "mediaconverter" {
  source        = "./modules/mediaconverter"
  s3_bucket_id  = module.s3.input_bucket_id
  s3_bucket_arn = module.s3.input_bucket_arn
  lambda_name   = "lambda_exec_media_converter"
}

#  clouf front do people can access website
module "cloudfront" {
  source                    = "./modules/cloudfront"
  output_bucket_domain_name = module.s3.output_bucket_domain_name
  output_bucket_id          = module.s3.output_bucket_id
}
