variable "aws_region" {
  default = "eu-west-1"
}

variable "workspace_start_cron" {
  default = "cron(0 8 ? * MON-FRI *)"
}

variable "workspace_stop_cron" {
  default = "cron(0 20 ? * MON-FRI *)"
}
