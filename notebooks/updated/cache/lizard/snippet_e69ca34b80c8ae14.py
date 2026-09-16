def _check_token_cache_type(self, cache_value):

    def check_string_value(name):
        return isinstance(cache_value[name], str) or isinstance(cache_value
            [name], unicode)

    def check_refresh_token():
        if 'refresh' in cache_value:
            return check_string_value('refresh')
        else:
            return True
    return (isinstance(cache_value, dict) and 'token' in cache_value and 
        'expires' in cache_value and check_string_value('token') and
        isinstance(cache_value['expires'], float) and check_refresh_token())