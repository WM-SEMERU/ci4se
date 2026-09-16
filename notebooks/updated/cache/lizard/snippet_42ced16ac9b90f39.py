def getschemas(cls):
    members = getmembers(cls, lambda member: isinstance(member, Schema))
    result = OrderedDict()
    for name, member in members:
        result[name] = member
    return result