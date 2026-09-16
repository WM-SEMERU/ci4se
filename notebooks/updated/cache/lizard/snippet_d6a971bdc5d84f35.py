def getTraceCombosByIds(self, trace_ids, adjust):
    self.send_getTraceCombosByIds(trace_ids, adjust)
    return self.recv_getTraceCombosByIds()