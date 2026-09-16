def set_values(self, columnName=None, rowList=None, table=None, value=None,
    verbose=None):
    PARAMS = set_param(['columnName', 'rowList', 'table', 'value'], [
        columnName, rowList, table, value])
    response = api(url=self.__url + '/set values', PARAMS=PARAMS, method=
        'POST', verbose=verbose)
    return response