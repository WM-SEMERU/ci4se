def _one_or_more_stages_remain(self, deploymentId):
    stages = __salt__['boto_apigateway.describe_api_stages'](restApiId=self
        .restApiId, deploymentId=deploymentId, **self._common_aws_args).get(
        'stages')
    return bool(stages)