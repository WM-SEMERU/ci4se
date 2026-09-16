def makeResponse(cls, objects, proto):
    tpt = objects.pop('__transport__')
    return _objectsToStrings(objects, cls.response, ConnectionStartBox(tpt),
        proto)