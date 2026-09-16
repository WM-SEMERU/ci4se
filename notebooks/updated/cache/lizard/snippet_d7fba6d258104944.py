def completedefault(self, text, line, *_):
    tokens = line.split()
    try:
        before = tokens[-2]
        complete = before.lower() in ('from', 'update', 'table', 'into')
        if tokens[0].lower() == 'dump':
            complete = True
        if complete:
            return [(t + ' ') for t in self.engine.cached_descriptions if t
                .startswith(text)]
    except KeyError:
        pass