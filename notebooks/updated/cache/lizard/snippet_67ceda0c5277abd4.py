def get_functions_auth_string(self, target_subscription_id):
    self._initialize_session()
    function_auth_variables = [constants.ENV_FUNCTION_TENANT_ID, constants.
        ENV_FUNCTION_CLIENT_ID, constants.ENV_FUNCTION_CLIENT_SECRET]
    if all(k in os.environ for k in function_auth_variables):
        auth = {'credentials': {'client_id': os.environ[constants.
            ENV_FUNCTION_CLIENT_ID], 'secret': os.environ[constants.
            ENV_FUNCTION_CLIENT_SECRET], 'tenant': os.environ[constants.
            ENV_FUNCTION_TENANT_ID]}, 'subscription': target_subscription_id}
    elif type(self.credentials) is ServicePrincipalCredentials:
        auth = {'credentials': {'client_id': os.environ[constants.
            ENV_CLIENT_ID], 'secret': os.environ[constants.
            ENV_CLIENT_SECRET], 'tenant': os.environ[constants.
            ENV_TENANT_ID]}, 'subscription': target_subscription_id}
    else:
        raise NotImplementedError(
            'Service Principal credentials are the only supported auth mechanism for deploying functions.'
            )
    return json.dumps(auth, indent=2)