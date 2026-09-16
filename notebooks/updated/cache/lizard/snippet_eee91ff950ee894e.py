def fromJSON(value):
    if isinstance(value, str):
        value = json.loads(value)
    elif isinstance(value, dict):
        pass
    else:
        raise AttributeError('Invalid input')
    return Extension(typeName=value['typeName'], capabilities=value[
        'capabilities'], enabled=value['enabled'] == 'true',
        maxUploadFileSize=value['maxUploadFileSize'], allowedUploadFileType
        =value['allowedUploadFileTypes'], properties=value['properties'])