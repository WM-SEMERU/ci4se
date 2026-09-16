def parse_branchset(self, branchset_node, depth, number, validate):
    uncertainty_type = branchset_node.attrib.get('uncertaintyType')
    filters = dict((filtername, branchset_node.attrib.get(filtername)) for
        filtername in self.FILTERS if filtername in branchset_node.attrib)
    if validate:
        self.validate_filters(branchset_node, uncertainty_type, filters)
    filters = self.parse_filters(branchset_node, uncertainty_type, filters)
    branchset = BranchSet(uncertainty_type, filters)
    if validate:
        self.validate_branchset(branchset_node, depth, number, branchset)
    return branchset