def terraform_external_data(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        query = json.loads(sys.stdin.read())
        validate(query)
        try:
            result = function(query, *args, **kwargs)
        except Exception as e:
            error('{}: {}'.format(type(e).__name__, e))
        validate(result)
        sys.stdout.write(json.dumps(result))
    return wrapper