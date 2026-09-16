def rest_error(self):
    error_json = self.__format_error('errors')
    return json.dumps(error_json, indent=1, sort_keys=True)