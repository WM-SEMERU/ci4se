def ssm_parameter_store(*parameters):
    if len(parameters) == 1 and not isinstance(parameters[0], basestring):
        parameters = parameters[0]

    def wrapper_wrapper(handler):

        @wraps(handler)
        def wrapper(event, context):
            ssm = boto3.client('ssm')
            if not hasattr(context, 'parameters'):
                context.parameters = {}
            for parameter in ssm.get_parameters(Names=parameters,
                WithDecryption=True)['Parameters']:
                context.parameters[parameter['Name']] = parameter['Value']
            return handler(event, context)
        return wrapper
    return wrapper_wrapper