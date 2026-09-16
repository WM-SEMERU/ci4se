def getPayloadStruct(self, payload):
    newSubItem = self.objType(self.api, 0, self.parentObjName, self.
        parentPayloadObj, self.parentKey, {})
    return newSubItem.getPayloadStruct(payload, self.parentPayloadObj)