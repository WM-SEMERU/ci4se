def disable_event(library, session, event_type, mechanism):
    return library.viDisableEvent(session, event_type, mechanism)