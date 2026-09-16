def createBamHeader(self, baseHeader):
    header = dict(baseHeader)
    newSequences = []
    for index, referenceInfo in enumerate(header['SQ']):
        if index < self.numChromosomes:
            referenceName = referenceInfo['SN']
            assert referenceName == self.chromosomes[index]
            newReferenceInfo = {'AS': self.referenceSetName, 'SN':
                referenceName, 'LN': 0, 'UR': 'http://example.com', 'M5':
                'dbb6e8ece0b5de29da56601613007c2a', 'SP': 'Human'}
            newSequences.append(newReferenceInfo)
    header['SQ'] = newSequences
    return header