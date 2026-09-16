def to_unicode(self, omit_final_dot=False):
    if len(self.labels) == 0:
        return '@'
    if len(self.labels) == 1 and self.labels[0] == '':
        return '.'
    if omit_final_dot and self.is_absolute():
        l = self.labels[:-1]
    else:
        l = self.labels
    s = '.'.join([encodings.idna.ToUnicode(_escapify(x)) for x in l])
    return s