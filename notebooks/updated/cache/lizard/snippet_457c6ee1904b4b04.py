def _get_events(self, result):
    events = []
    for event_data in result:
        event = Event.factory(event_data)
        if event is not None:
            events.append(event)
            if isinstance(event, DeviceStateChangedEvent):
                if self.__devices[event.device_url] is None:
                    raise Exception('Received device change ' +
                        "state for unknown device '" + event.device_url + "'")
                self.__devices[event.device_url].set_active_states(event.states
                    )
    return events