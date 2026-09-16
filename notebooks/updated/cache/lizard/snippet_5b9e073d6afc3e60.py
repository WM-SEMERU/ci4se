def included(self, start, stop):
    for event in self:
        if start <= event.begin <= stop and start <= event.end <= stop:
            yield event