def update_lambda_configuration(self, lambda_arn, function_name, handler,
    description='Zappa Deployment', timeout=30, memory_size=512, publish=
    True, vpc_config=None, runtime='python2.7', aws_environment_variables=
    None, aws_kms_key_arn=None):
    print('Updating Lambda function configuration..')
    if not vpc_config:
        vpc_config = {}
    if not self.credentials_arn:
        self.get_credentials_arn()
    if not aws_kms_key_arn:
        aws_kms_key_arn = ''
    if not aws_environment_variables:
        aws_environment_variables = {}
    lambda_aws_config = self.lambda_client.get_function_configuration(
        FunctionName=function_name)
    if 'Environment' in lambda_aws_config:
        lambda_aws_environment_variables = lambda_aws_config['Environment'
            ].get('Variables', {})
        for key, value in lambda_aws_environment_variables.items():
            if key not in aws_environment_variables:
                aws_environment_variables[key] = value
    response = self.lambda_client.update_function_configuration(FunctionName
        =function_name, Runtime=runtime, Role=self.credentials_arn, Handler
        =handler, Description=description, Timeout=timeout, MemorySize=
        memory_size, VpcConfig=vpc_config, Environment={'Variables':
        aws_environment_variables}, KMSKeyArn=aws_kms_key_arn,
        TracingConfig={'Mode': 'Active' if self.xray_tracing else
        'PassThrough'})
    resource_arn = response['FunctionArn']
    if self.tags:
        self.lambda_client.tag_resource(Resource=resource_arn, Tags=self.tags)
    return resource_arn