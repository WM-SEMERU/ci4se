def add_template_events(self, columns, vectors):
    new_events = None
    for v in vectors:
        if v is not None:
            new_events = numpy.zeros(len(v), dtype=self.event_dtype)
            break
    assert new_events is not None
    new_events['template_id'] = self.template_index
    for c, v in zip(columns, vectors):
        if v is not None:
            if isinstance(v, Array):
                new_events[c] = v.numpy()
            else:
                new_events[c] = v
    self.template_events = numpy.append(self.template_events, new_events)