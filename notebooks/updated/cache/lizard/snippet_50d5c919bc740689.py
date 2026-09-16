def is_event_of_key_string(event, key_string):
    return len(event) >= 2 and not isinstance(event[1], Gdk.ModifierType
        ) and event[0] == Gtk.accelerator_parse(key_string)[0]