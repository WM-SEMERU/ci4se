def _checkFunctioncode(functioncode, listOfAllowedValues=[]):
    FUNCTIONCODE_MIN = 1
    FUNCTIONCODE_MAX = 127
    _checkInt(functioncode, FUNCTIONCODE_MIN, FUNCTIONCODE_MAX, description
        ='functioncode')
    if listOfAllowedValues is None:
        return
    if not isinstance(listOfAllowedValues, list):
        raise TypeError(
            'The listOfAllowedValues should be a list. Given: {0!r}'.format
            (listOfAllowedValues))
    for value in listOfAllowedValues:
        _checkInt(value, FUNCTIONCODE_MIN, FUNCTIONCODE_MAX, description=
            'functioncode inside listOfAllowedValues')
    if functioncode not in listOfAllowedValues:
        raise ValueError('Wrong function code: {0}, allowed values are {1!r}'
            .format(functioncode, listOfAllowedValues))