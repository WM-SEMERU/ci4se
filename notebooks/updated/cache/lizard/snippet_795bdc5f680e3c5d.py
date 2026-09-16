def add_request_ids_from_environment(logger, name, event_dict):
    if ENV_APIG_REQUEST_ID in os.environ:
        event_dict['api_request_id'] = os.environ[ENV_APIG_REQUEST_ID]
    if ENV_LAMBDA_REQUEST_ID in os.environ:
        event_dict['lambda_request_id'] = os.environ[ENV_LAMBDA_REQUEST_ID]
    return event_dict