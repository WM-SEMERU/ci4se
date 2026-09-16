def processIqRegistry(self, entity):
    if entity.getTag() == 'iq':
        iq_id = entity.getId()
        if iq_id in self.iqRegistry:
            originalIq, successClbk, errorClbk = self.iqRegistry[iq_id]
            del self.iqRegistry[iq_id]
            if entity.getType(
                ) == IqProtocolEntity.TYPE_RESULT and successClbk:
                successClbk(entity, originalIq)
            elif entity.getType() == IqProtocolEntity.TYPE_ERROR and errorClbk:
                errorClbk(entity, originalIq)
            return True
    return False