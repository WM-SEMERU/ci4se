def _BreakpointEvent(self, event, frame):
    error_status = None
    if event != native.BREAKPOINT_EVENT_HIT:
        error_status = _BREAKPOINT_EVENT_STATUS[event]
    elif self.definition.get('action') == 'LOG':
        error_status = self._collector.Log(frame)
        if not error_status:
            return
    if not self._SetCompleted():
        return
    self.Clear()
    if error_status:
        self._CompleteBreakpoint({'status': error_status})
        return
    collector = capture_collector.CaptureCollector(self.definition, self.
        data_visibility_policy)
    try:
        collector.Collect(frame)
    except BaseException as e:
        native.LogInfo('Internal error during data capture: %s' % repr(e))
        error_status = {'isError': True, 'description': {'format': 
            'Internal error while capturing data: %s' % repr(e)}}
        self._CompleteBreakpoint({'status': error_status})
        return
    except:
        native.LogInfo('Unknown exception raised')
        error_status = {'isError': True, 'description': {'format':
            'Unknown internal error'}}
        self._CompleteBreakpoint({'status': error_status})
        return
    self._CompleteBreakpoint(collector.breakpoint, is_incremental=False)