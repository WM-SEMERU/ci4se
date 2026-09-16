def get_short_name(self):
    sname = osp.splitext(osp.basename(self.filename))[0]
    if len(sname) > 20:
        fm = QFontMetrics(QFont())
        sname = fm.elidedText(sname, Qt.ElideRight, 110)
    return sname