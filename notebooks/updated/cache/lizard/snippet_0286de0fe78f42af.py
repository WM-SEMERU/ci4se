def addSubsumableToGroups(self, proteinIds, groupIds):
    for groupId in AUX.toList(groupIds):
        self.groups[groupId].addSubsumableProteins(proteinIds)
        self._addProteinIdsToGroupMapping(proteinIds, groupId)