def current_segment(self):
    entity = self.get_trace_entity()
    if self._is_subsegment(entity):
        return entity.parent_segment
    else:
        return entity