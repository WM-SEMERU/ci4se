def dpar(self, cl=1):
    sval = list(map(self.toString, self.value, len(self.value) * [1]))
    for i in range(len(sval)):
        if sval[i] == '':
            sval[i] = 'None'
    s = '%s = [%s]' % (self.name, ', '.join(sval))
    return s