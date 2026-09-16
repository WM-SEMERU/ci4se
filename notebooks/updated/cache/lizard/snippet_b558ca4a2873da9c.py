def _addProteinIdsToGroupMapping(self, proteinIds, groupId):
    for proteinId in AUX.toList(proteinIds):
        self._proteinToGroupIds[proteinId].add(groupId)