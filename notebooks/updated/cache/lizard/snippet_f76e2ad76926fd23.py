def end_segment(self, end_time=None):
    entity = self.get_trace_entity()
    if not entity:
        log.warning('No segment to end')
        return
    if self._is_subsegment(entity):
        entity.parent_segment.close(end_time)
    else:
        entity.close(end_time)