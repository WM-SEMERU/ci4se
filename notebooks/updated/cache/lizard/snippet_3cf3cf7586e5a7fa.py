def _get_table_info(self):
    self.fields = []
    self.field_info = {}
    self.cursor.execute('PRAGMA table_info (%s)' % self.name)
    for field_info in self.cursor.fetchall():
        fname = field_info[1].encode('utf-8')
        self.fields.append(fname)
        ftype = field_info[2].encode('utf-8')
        info = {'type': ftype}
        info['NOT NULL'] = field_info[3] != 0
        default = field_info[4]
        if isinstance(default, unicode):
            default = guess_default_fmt(default)
        info['DEFAULT'] = default
        self.field_info[fname] = info