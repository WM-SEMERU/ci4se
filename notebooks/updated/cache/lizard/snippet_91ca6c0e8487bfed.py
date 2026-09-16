def _api_args(self):
    response.content_type = 'application/json; charset=utf-8'
    try:
        args_json = json.dumps(vars(self.args))
    except Exception as e:
        abort(404, 'Cannot get args (%s)' % str(e))
    return args_json