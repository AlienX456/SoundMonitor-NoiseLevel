module "noise_level" {
  source = "git::https://github.com/AlienX456/SoundMonitor-IAC-Infrastructure-Common.git//use-cases/ecs_s3_kafka_services?ref=3.0.7-rc"

  // User vars
  cpu             = "256"
  device_selector = "cpu"
  memory          = "512"
  number_of_tasks = "1"
  process-type    = "audio"
  mapper_url      = ""

  // IAC VARS
  aws_provider_key           = var.aws_provider_key
  aws_provider_secret        = var.aws_provider_secret
  aws_ecr_account_url        = var.aws_ecr_account_url
  ecr_image_tag              = var.ecr_image_tag
  kafka_bootstrap_server_one = var.kafka_bootstrap_server_one
  repository_name            = var.repository_name
}