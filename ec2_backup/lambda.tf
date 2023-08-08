resource "aws_lambda_function" "ami_backup_cleanup" {
  filename      = "ami_backup.zip"
  function_name = "ami-backup-cleanup"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
}
