def is_parent_of_objective(self, id_=None, objective_id=None):
    if id_ is None or objective_id is None:
        raise NullArgument()
    return id_ in list(self.get_parent_objective_ids(objective_id))