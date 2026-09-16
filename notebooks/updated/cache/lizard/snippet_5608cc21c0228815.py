def getTraceTimelinesByIds(self, trace_ids, adjust):
    self.send_getTraceTimelinesByIds(trace_ids, adjust)
    return self.recv_getTraceTimelinesByIds()