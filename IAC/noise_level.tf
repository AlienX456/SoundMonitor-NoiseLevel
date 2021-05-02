module "noise_level" {
  source = "git::https://github.com/AlienX456/SoundMonitor-IAC-Infrastructure-Common.git//on-ecs-processing"

  cluster-name= var.cluster-name
  service-name= "monitor-noiselevel-service"
  family-name = "monitor-noiselevel"
  soundmonitor_mainsubnet= var.soundmonitor_mainsubnet
  cpu= "256"
  memory= "512"

  aws_region= "us-east-1"
  aws_provider_key= var.aws_provider_key
  aws_provider_secret= var.aws_provider_secret

  aws_inferencer_key= var.aws_inferencer_key
  aws_inferencer_secret= var.aws_inferencer_secret
  mapper_url = ""

  kafka_group_id= "noise-level"
  kafka_data_upload_event= var.kafka_data_upload_event
  kafka_process_result_event= var.kafka_process_result_event
  kafka_encode_format= var.kafka_encode_format
  kafka_bootstrap_server_one= var.kafka_bootstrap_server_one

  ecr_image_tag= var.ecr_image_tag
  ecr_image_repo= var.ecr_image_repo
  records_bucket_name= var.records_bucket_name

  device_selector= "cpu"
}