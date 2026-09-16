def get_id2gos(self, **kws):
    if len(self.taxid2asscs) == 1:
        taxid = next(iter(self.taxid2asscs.keys()))
        return self._get_id2gos(self.taxid2asscs[taxid], **kws)
    assert 'taxid' in kws, "**FATAL: 'taxid' NOT FOUND IN Gene2GoReader::get_id2gos({KW})".format(
        KW=kws)
    taxid = kws['taxid']
    assert taxid in self.taxid2asscs, '**FATAL: TAXID({T}) DATA MISSING'.format(
        T=taxid)
    return self._get_id2gos(self.taxid2asscs[taxid], **kws)