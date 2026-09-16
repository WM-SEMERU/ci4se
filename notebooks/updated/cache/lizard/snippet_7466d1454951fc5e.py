def getdesc(self, actual=True):
    tabledesc = self._getdesc(actual, True)
    hcdefs = tabledesc.get('_define_hypercolumn_', {})
    for c, hcdef in hcdefs.iteritems():
        if 'HCcoordnames' in hcdef and len(hcdef['HCcoordnames']) == 0:
            del hcdef['HCcoordnames']
        if 'HCidnames' in hcdef and len(hcdef['HCidnames']) == 0:
            del hcdef['HCidnames']
    return tabledesc