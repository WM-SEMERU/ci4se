def update(self, default_activity_sid=values.unset, event_callback_url=
    values.unset, events_filter=values.unset, friendly_name=values.unset,
    multi_task_enabled=values.unset, timeout_activity_sid=values.unset,
    prioritize_queue_order=values.unset):
    return self._proxy.update(default_activity_sid=default_activity_sid,
        event_callback_url=event_callback_url, events_filter=events_filter,
        friendly_name=friendly_name, multi_task_enabled=multi_task_enabled,
        timeout_activity_sid=timeout_activity_sid, prioritize_queue_order=
        prioritize_queue_order)