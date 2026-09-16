def update(self, other):
    if not isinstance(other, CtsTextgroupMetadata):
        raise TypeError('Cannot add %s to CtsTextgroupMetadata' % type(other))
    elif str(self.urn) != str(other.urn):
        raise InvalidURN(
            'Cannot add CtsTextgroupMetadata %s to CtsTextgroupMetadata %s ' %
            (self.urn, other.urn))
    for urn, work in other.works.items():
        if urn in self.works:
            self.works[urn].update(deepcopy(work))
        else:
            self.works[urn] = deepcopy(work)
        self.works[urn].parent = self
        self.works[urn].resource = None
    return self