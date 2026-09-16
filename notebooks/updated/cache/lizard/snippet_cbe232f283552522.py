def remove_dependency(self, p_from_todo, p_to_todo, p_leave_tags=False):
    dep_id = p_from_todo.tag_value('id')
    if dep_id:
        self._depgraph.remove_edge(hash(p_from_todo), hash(p_to_todo))
        self.dirty = True
    if dep_id and not p_leave_tags:
        p_to_todo.remove_tag('p', dep_id)
        if not self.children(p_from_todo, True):
            p_from_todo.remove_tag('id')
            del self._parentdict[dep_id]