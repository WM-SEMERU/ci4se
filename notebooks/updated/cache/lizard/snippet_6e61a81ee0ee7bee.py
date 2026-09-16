def relation_exists(self, parent, child, relation_type):
    return PIDRelation.query.filter_by(child_pid_id=child.id, parent_pid_id
        =parent.id, relation_type=relation_type).count() > 0