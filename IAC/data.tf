
variable "aws_provider_key" {
  description = "AWS key for deploy and infrastructure providing"
}

variable "aws_provider_secret" {
  description = "AWS secret for deploy and infrastructure providing"
}

variable "ecr_image_tag" {
  description = "Inferencer latest image tag"
}

variable "records_bucket_name" {
  description =  "audio files bucket NAME"
}

variable "kafka_upload_topic_name" {
  description = "Kafka event of data uploading"
}

variable "kafka_result_topic_name" {
  description = "Kafka event of process reult"
}
variable "ecr_image_repo" {
  description = "Inferencer repo"
}

variable "kafka_bootstrap_server_one" {
  description =  "Endpoint of kafka server one"
}

variable "mapper_url" {
  default = "url of mapper"
}

