def unbind(self, *args):
    props = self.__property_events.values()
    events = self.__events.values()
    for arg in args:
        for prop in props:
            prop.remove_listener(arg)
        for e in events:
            e.remove_listener(arg)