def append(self, payload):
    if self.objType.setInParentPayload:
        print('Error, {} is not elibible to addition, but only set'.format(
            self.objName))
        return False
    ret = self.api.create('{}/{}/{}'.format(self.parentObjName, self.
        parentKey, self.objNameSet), self.getPayloadStruct(payload))
    return ret