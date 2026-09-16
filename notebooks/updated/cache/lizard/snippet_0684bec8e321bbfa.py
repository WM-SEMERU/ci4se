def get_groups(self, **kwargs):
    params = {'cultureInfo': util.language_code(kwargs.get('lang'))}
    result = self.make_request('geo', 'get_groups', **params)
    if not util.check_result(result):
        return False, result.get('resultDescription', 'UNKNOWN ERROR')
    values = util.response_list(result, 'resultValues')
    return True, [emtype.GeoGroupItem(**a) for a in values]