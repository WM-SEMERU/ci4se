def get_lambda_function(self, function_name):
    response = self.lambda_client.get_function(FunctionName=function_name)
    return response['Configuration']['FunctionArn']