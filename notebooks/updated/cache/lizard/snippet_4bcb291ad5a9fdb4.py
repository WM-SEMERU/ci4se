def get_file_history(self, path, limit=None):
    fctx = self._get_filectx(path)
    hist = []
    cnt = 0
    for cs in reversed([x for x in fctx.filelog()]):
        cnt += 1
        hist.append(hex(fctx.filectx(cs).node()))
        if limit and cnt == limit:
            break
    return [self.repository.get_changeset(node) for node in hist]