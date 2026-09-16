def _get_current_deployment_id(self):
    deploymentId = ''
    stage = __salt__['boto_apigateway.describe_api_stage'](restApiId=self.
        restApiId, stageName=self._stage_name, **self._common_aws_args).get(
        'stage')
    if stage:
        deploymentId = stage.get('deploymentId')
    return deploymentId