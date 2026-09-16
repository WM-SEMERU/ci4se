def match_objective_id(self, objective_id, match):
    if not isinstance(objective_id, Id):
        raise errors.InvalidArgument()
    self._add_match('objectiveId', str(objective_id), match)