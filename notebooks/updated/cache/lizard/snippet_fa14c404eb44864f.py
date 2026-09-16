def getOperationName(id: str):
    if isinstance(id, str):
        assert id in operations.keys(), 'Unknown operation {}'.format(id)
        return id
    elif isinstance(id, int):
        return getOperationNameForId(id)
    else:
        raise ValueError