def bind(self, **kwargs):
    aio_loop = kwargs.pop('__aio_loop__', None)
    props = self.__property_events
    events = self.__events
    for name, cb in kwargs.items():
        if name in props:
            e = props[name]
        else:
            e = events[name]
        e.add_listener(cb, __aio_loop__=aio_loop)