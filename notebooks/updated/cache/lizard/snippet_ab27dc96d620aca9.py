def _reprJSON(self):
    return {'__PepSeq__': [self.sequence, self.missedCleavage, self.
        isUnique, list(self.proteins), self.proteinPositions]}