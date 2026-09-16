def team(self, name=None, id=None, is_hidden=False, **kwargs):
    _teams = self.teams(name=name, id=id, **kwargs)
    if len(_teams) == 0:
        raise NotFoundError('No team criteria matches')
    if len(_teams) != 1:
        raise MultipleFoundError('Multiple teams fit criteria')
    return _teams[0]