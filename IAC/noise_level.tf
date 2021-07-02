module "noise_level" {
  source = "git::https://github.com/AlienX456/SoundMonitor-IAC-Infrastructure-Common.git//ecs_s3_kafka_services"

  service-name= "noise-level-service"
  family-name = "noise-level-adapa"
  cpu= "256"
  memory= "512"
  number_of_tasks="1"

  aws_provider_key= var.aws_provider_key
  aws_provider_secret= var.aws_provider_secret

  mapper_url = var.mapper_url

  kafka_group_id= "noise-group"
  kafka_upload_topic_name= var.kafka_upload_topic_name
  kafka_result_topic_name= var.kafka_result_topic_name
  kafka_bootstrap_server_one= var.kafka_bootstrap_server_one

  ecr_image_tag= var.ecr_image_tag
  ecr_image_repo= var.ecr_image_repo
  records_bucket_name= var.records_bucket_name

  device_selector= "cpu"
}