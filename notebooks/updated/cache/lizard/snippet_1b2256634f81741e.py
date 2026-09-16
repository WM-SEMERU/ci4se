def findNodeById(self, objectId):
    for item in self.items():
        if isinstance(item, XNode) and item.objectId() == objectId:
            return item
    return None