def process_embedded(self, xlist, anexec, add=True):
    delta = 0
    for t in anexec.types:
        key = '{}.{}'.format(anexec.name, t)
        if key in xlist:
            docs = self.to_doc(xlist[key][0], t)
            self.process_memberdocs(docs, anexec.types[t], add)
            anexec.types[t].docstart = xlist[key][1]
            delta += xlist[key][2] - anexec.types[t].docend
            anexec.types[t].docend = xlist[key][2]
    for iexec in anexec.executables:
        key = '{}.{}'.format(anexec.name, iexec)
        if key in xlist:
            docs = self.to_doc(xlist[key][0], t)
            self.process_memberdocs(docs, anexec.executables[iexec], add)
            anexec.executables[iexec].docstart = xlist[key][1]
            delta += xlist[key][2] - anexec.executables[iexec].docend
            anexec.executables[iexec].docend = xlist[key][2]
    if not add:
        return delta