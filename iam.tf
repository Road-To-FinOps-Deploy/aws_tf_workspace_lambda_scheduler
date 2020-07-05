resource "aws_iam_role" "iam_role_for_workspace_start_stop" {
  name               = "${var.function_prefix}iam_role_workspace_start_stop"
  assume_role_policy = file("${path.module}/policies/LambdaAssume.pol")
}

resource "aws_iam_role_policy" "iam_role_policy_for_workspace_start_stop" {
  name   = "${var.function_prefix}ExecuteLambda"
  role   = aws_iam_role.iam_role_for_workspace_start_stop.id
  policy = file("${path.module}/policies/LambdaExecution.pol")
}

