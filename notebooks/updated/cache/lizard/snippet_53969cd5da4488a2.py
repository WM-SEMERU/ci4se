def checkInputParameter(method, parameters, validParameters,
    requiredParameters=None):
    for parameter in parameters:
        if parameter not in validParameters:
            raise dbsClientException('Invalid input', 
                'API %s does not support parameter %s. Supported parameters are %s'
                 % (method, parameter, validParameters))
    if requiredParameters is not None:
        if 'multiple' in requiredParameters:
            match = False
            for requiredParameter in requiredParameters['multiple']:
                if (requiredParameter != 'detail' and requiredParameter in
                    parameters):
                    match = True
                    break
            if not match:
                raise dbsClientException('Invalid input', 
                    'API %s does require one of the parameters %s' % (
                    method, requiredParameters['multiple']))
        if 'forced' in requiredParameters:
            for requiredParameter in requiredParameters['forced']:
                if requiredParameter not in parameters:
                    raise dbsClientException('Invalid input', 
                        'API %s does require the parameter %s. Forced required parameters are %s'
                         % (method, requiredParameter, requiredParameters[
                        'forced']))
        if 'standalone' in requiredParameters:
            overlap = []
            for requiredParameter in requiredParameters['standalone']:
                if requiredParameter in parameters:
                    overlap.append(requiredParameter)
            if len(overlap) != 1:
                raise dbsClientException('Invalid input', 
                    'API %s does requires only *one* of the parameters %s.' %
                    (method, requiredParameters['standalone']))