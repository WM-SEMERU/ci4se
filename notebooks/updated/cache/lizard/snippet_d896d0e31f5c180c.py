def begin_subsegment(self, name, namespace='local'):
    segment = self.current_segment()
    if not segment:
        log.warning('No segment found, cannot begin subsegment %s.' % name)
        return None
    if not segment.sampled:
        subsegment = DummySubsegment(segment, name)
    else:
        subsegment = Subsegment(name, namespace, segment)
    self.context.put_subsegment(subsegment)
    return subsegment