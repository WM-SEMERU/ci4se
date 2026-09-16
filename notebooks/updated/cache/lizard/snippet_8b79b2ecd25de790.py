def MapParamNames(params, request_type):
    return [(encoding.GetCustomJsonFieldMapping(request_type, json_name=p) or
        p) for p in params]