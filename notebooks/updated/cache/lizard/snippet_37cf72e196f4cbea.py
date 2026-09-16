def get_object_cat1(con, token, cat, kwargs):
    req_str = '/' + kwargs['id'] + '?'
    req_str += 'access_token=' + token
    del kwargs['id']
    key = settings.get_object_cat1_param[cat]
    req_str += '&' + key + '='
    if key in kwargs.keys():
        length = len(kwargs[key])
        for i in range(length):
            if i == 0:
                req_str += kwargs[key][i]
            else:
                req_str += ',' + kwargs[key][i]
    else:
        return 'Parameter Error'
    res = wiring.send_request('GET', con, req_str, '')
    return res