def transform(self, fseries, norm=True, epoch=None, search=None):
    out = []
    for qtile in self:
        out.append(qtile.transform(fseries, norm=norm, epoch=epoch))
    return QGram(self, out, search)