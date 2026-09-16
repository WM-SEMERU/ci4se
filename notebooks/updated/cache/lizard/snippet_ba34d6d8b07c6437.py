def create_guid(self, collection=None):
    guid = str(uuid.uuid4())
    if collection:
        return str.join('/', [collection, guid])
    else:
        return guid