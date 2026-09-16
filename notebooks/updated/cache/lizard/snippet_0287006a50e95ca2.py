def dial(self, number=None, action=None, method=None, timeout=None,
    hangup_on_star=None, time_limit=None, caller_id=None, record=None, trim
    =None, recording_status_callback=None, recording_status_callback_method
    =None, recording_status_callback_event=None, answer_on_bridge=None,
    ring_tone=None, **kwargs):
    return self.nest(Dial(number=number, action=action, method=method,
        timeout=timeout, hangup_on_star=hangup_on_star, time_limit=
        time_limit, caller_id=caller_id, record=record, trim=trim,
        recording_status_callback=recording_status_callback,
        recording_status_callback_method=recording_status_callback_method,
        recording_status_callback_event=recording_status_callback_event,
        answer_on_bridge=answer_on_bridge, ring_tone=ring_tone, **kwargs))