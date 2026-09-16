def to_cloudformation(self):
    rest_api = self._construct_rest_api()
    deployment = self._construct_deployment(rest_api)
    swagger = None
    if rest_api.Body is not None:
        swagger = rest_api.Body
    elif rest_api.BodyS3Location is not None:
        swagger = rest_api.BodyS3Location
    stage = self._construct_stage(deployment, swagger)
    permissions = self._construct_authorizer_lambda_permission()
    return rest_api, deployment, stage, permissions