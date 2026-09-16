def is_lambda_error_response(lambda_response):
    is_lambda_user_error_response = False
    try:
        lambda_response_dict = json.loads(lambda_response)
        if (isinstance(lambda_response_dict, dict) and len(
            lambda_response_dict) == 3 and 'errorMessage' in
            lambda_response_dict and 'errorType' in lambda_response_dict and
            'stackTrace' in lambda_response_dict):
            is_lambda_user_error_response = True
    except ValueError:
        pass
    return is_lambda_user_error_response