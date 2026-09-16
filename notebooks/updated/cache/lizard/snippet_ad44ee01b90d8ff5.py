def set_learning_objectives(self, objective_ids):
    if not isinstance(objective_ids, list):
        raise errors.InvalidArgument()
    if self.get_learning_objectives_metadata().is_read_only():
        raise errors.NoAccess()
    idstr_list = []
    for object_id in objective_ids:
        if not self._is_valid_id(object_id):
            raise errors.InvalidArgument()
        idstr_list.append(str(object_id))
    self._my_map['learningObjectiveIds'] = idstr_list