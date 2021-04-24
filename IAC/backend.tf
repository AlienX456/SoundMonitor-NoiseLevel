terraform {
  backend "s3" {
    bucket  = "terraform-monitor-provide-states-files"
    key     = "noiseLevel.tfstate"
    region  = "us-east-1"
  }
}