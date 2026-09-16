def addReadGroup(self, readGroup):
    id_ = readGroup.getId()
    self._readGroupIdMap[id_] = readGroup
    self._readGroupIds.append(id_)