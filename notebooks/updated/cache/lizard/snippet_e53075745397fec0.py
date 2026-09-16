def insert_child(self, child_pid, index=-1):
    self._check_child_limits(child_pid)
    if index is None:
        index = -1
    try:
        with db.session.begin_nested():
            if not isinstance(child_pid, PersistentIdentifier):
                child_pid = resolve_pid(child_pid)
            child_relations = self._resolved_pid.child_relations.filter(
                PIDRelation.relation_type == self.relation_type.id).order_by(
                PIDRelation.index).all()
            relation_obj = PIDRelation.create(self._resolved_pid, child_pid,
                self.relation_type.id, None)
            if index == -1:
                child_relations.append(relation_obj)
            else:
                child_relations.insert(index, relation_obj)
            for idx, c in enumerate(child_relations):
                c.index = idx
    except IntegrityError:
        raise PIDRelationConsistencyError('PID Relation already exists.')