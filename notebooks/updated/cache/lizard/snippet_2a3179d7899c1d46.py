def export(self, top=True):
    out = []
    if top:
        out.append(self._internal_name)
    out.append(self._to_str(self.comments_2))
    return ','.join(out)