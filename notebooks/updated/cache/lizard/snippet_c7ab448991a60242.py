def fromJSON(value):
    j = json.loads(value)
    v = GPMultiValue(gptype=j['dataType'])
    if 'defaultValue' in j:
        v.value = j['defaultValue']
    else:
        v.value = j['value']
    if 'paramName' in j:
        v.paramName = j['paramName']
    elif 'name' in j:
        v.paramName = j['name']
    return v