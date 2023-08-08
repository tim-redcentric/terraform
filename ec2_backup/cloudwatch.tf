resource "aws_cloudwatch_event_rule" "ami_backup_rule" {
  name        = "ami-backup-cleanup-rule"
  description = "Trigger Lambda function for AMI backup and cleanup"
  schedule_expression = "rate(1 day)"
}

resource "aws_cloudwatch_event_target" "ami_backup_target" {
  rule      = aws_cloudwatch_event_rule.ami_backup_rule.name
  target_id = "ami-backup-target"
  arn       = aws_lambda_function.ami_backup_cleanup.arn
}
