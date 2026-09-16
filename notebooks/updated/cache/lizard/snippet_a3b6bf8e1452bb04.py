def from_events(self, instance, ev_args, ctx):
    tag = ev_args[0], ev_args[1]
    cls = self._tag_map[tag]
    obj = yield from cls.parse_events(ev_args, ctx)
    mapping = self.__get__(instance, type(instance))
    mapping[self.key(obj)].append(obj)