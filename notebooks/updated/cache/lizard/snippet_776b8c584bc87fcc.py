def _get_keys(self, read, input_records):
    for i in range(read.value):
        ir = input_records[i]
        if ir.EventType in EventTypes:
            ev = getattr(ir.Event, EventTypes[ir.EventType])
            if type(ev) == KEY_EVENT_RECORD and ev.KeyDown:
                for key_press in self._event_to_key_presses(ev):
                    yield key_press
            elif type(ev) == MOUSE_EVENT_RECORD:
                for key_press in self._handle_mouse(ev):
                    yield key_press