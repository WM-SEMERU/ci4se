def isempty(result):
    if isinstance(result, list):
        for element in result:
            if isinstance(element, list):
                if not isempty(element):
                    return False
            elif element is not None:
                return False
    elif result is not None:
        return False
    return True