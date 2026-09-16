def dict(self):
    collection = super().dict()
    serialized_items = []
    for item in collection['items']:
        serialized_items.append(self.serializer(item))
    collection['items'] = serialized_items
    return collection