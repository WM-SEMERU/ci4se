def peek(quantity, min_type=EventType.firstevent, max_type=EventType.lastevent
    ):
    return _peep(quantity, lib.SDL_PEEKEVENT, min_type, max_type)