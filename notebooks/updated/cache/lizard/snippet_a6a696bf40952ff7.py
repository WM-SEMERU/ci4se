def filter(self, media_type, **params):
    mtype, msubtype = self._split_media_type(media_type)
    for x in self.__iter__():
        matched = True
        for k, v in params.items():
            if x[2].get(k, None) != v:
                matched = False
                break
        if matched:
            if x[0][0] == '*':
                if x[0][1] == '*':
                    yield x
                elif x[0][1] == msubtype:
                    yield x
            elif mtype == '*':
                if msubtype == '*':
                    yield x
                elif x[0][1] == msubtype:
                    yield x
            elif x[0][0] == mtype:
                if msubtype == '*':
                    yield x
                elif x[0][1] == '*':
                    yield x
                elif x[0][1] == msubtype:
                    yield x