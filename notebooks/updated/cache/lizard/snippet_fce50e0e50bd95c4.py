def add_subgroups(self, subgroups):
    if subgroups is None:
        subgroups = {}
    _subgroups = {}
    for sg in subgroups:
        assert isinstance(sg, SubGroupDefinition)
        _subgroups[sg.name] = sg
    self.subgroups = _subgroups