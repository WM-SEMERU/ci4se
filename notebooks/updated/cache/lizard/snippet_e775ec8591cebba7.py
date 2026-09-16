def match_learning_objective_id(self, objective_id, match):
    self._add_match('learningObjectiveIds', str(objective_id), bool(match))