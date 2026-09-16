def getDependents(self, retracted=False):

    def is_dependent(analysis):
        calculation = analysis.getCalculation()
        if not calculation:
            return False
        services = calculation.getRawDependentServices()
        if not services:
            return False
        query = dict(UID=services, getKeyword=self.getKeyword())
        services = api.search(query, 'bika_setup_catalog')
        return len(services) > 0
    siblings = self.getSiblings(retracted=retracted)
    return filter(lambda sib: is_dependent(sib), siblings)