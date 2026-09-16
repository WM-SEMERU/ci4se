def _canBeExpanded(self, headVerbRoot, headVerbWID,
    suitableNomAdvExpansions, expansionVerbs, widToToken):
    if len(suitableNomAdvExpansions) == 1 and expansionVerbs:
        suitableExpansionVerbs = [expVerb for expVerb in expansionVerbs if 
            expVerb[2] == suitableNomAdvExpansions[0][2]]
        if len(suitableExpansionVerbs) == 1:
            nomAdvWID = suitableNomAdvExpansions[0][0]
            if self._isLikelyNotPhrase(headVerbRoot, headVerbWID, nomAdvWID,
                widToToken):
                return suitableExpansionVerbs[0]
    return None