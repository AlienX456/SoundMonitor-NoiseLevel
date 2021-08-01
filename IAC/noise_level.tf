module "noise_level" {
  
  source = "git::https://github.com/AlienX456/SoundMonitor-IAC-Infrastructure-Common.git//ecs_s3_kafka_services?ref=2.2.0"

  service-name= "${var.service_name}-service"
  family_name = var.service_name
  cpu= "256"
  memory= "512"
  number_of_tasks="1"

  aws_provider_key= var.aws_provider_key
  aws_provider_secret= var.aws_provider_secret

  mapper_url = ""

  kafka_group_id= "noise-group"
  kafka_upload_topic_name= var.kafka_upload_topic_name
  kafka_result_topic_name= var.kafka_result_topic_name
  kafka_bootstrap_server_one= var.kafka_bootstrap_server_one

  ecr_image_tag= var.ecr_image_tag
  aws_ecr_account_url = var.aws_ecr_account_url
  records_bucket_name= var.records_bucket_name
  index_name = var.index_name

  device_selector= "cpu"
}