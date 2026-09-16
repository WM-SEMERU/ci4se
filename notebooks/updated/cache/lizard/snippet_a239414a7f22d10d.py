def check_headers(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method in ('POST', 'PATCH'):
            if ('Content-Type' in request.headers and 
                'application/vnd.api+json' in request.headers[
                'Content-Type'] and request.headers['Content-Type'] !=
                'application/vnd.api+json'):
                error = json.dumps(jsonapi_errors([{'source': '', 'detail':
                    'Content-Type header must be application/vnd.api+json',
                    'title': 'Invalid request header', 'status': '415'}]),
                    cls=JSONEncoder)
                return make_response(error, 415, {'Content-Type':
                    'application/vnd.api+json'})
        if 'Accept' in request.headers:
            flag = False
            for accept in request.headers['Accept'].split(','):
                if accept.strip() == 'application/vnd.api+json':
                    flag = False
                    break
                if 'application/vnd.api+json' in accept and accept.strip(
                    ) != 'application/vnd.api+json':
                    flag = True
            if flag is True:
                error = json.dumps(jsonapi_errors([{'source': '', 'detail':
                    'Accept header must be application/vnd.api+json withoutmedia type parameters'
                    , 'title': 'Invalid request header', 'status': '406'}]),
                    cls=JSONEncoder)
                return make_response(error, 406, {'Content-Type':
                    'application/vnd.api+json'})
        return func(*args, **kwargs)
    return wrapper