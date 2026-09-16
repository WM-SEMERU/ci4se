def UnregisterFlowProcessingHandler(self, timeout=None):
    self.flow_handler_target = None
    if self.flow_handler_thread:
        self.flow_handler_stop = True
        self.flow_handler_thread.join(timeout)
        if self.flow_handler_thread.isAlive():
            raise RuntimeError('Flow processing handler did not join in time.')
        self.flow_handler_thread = None