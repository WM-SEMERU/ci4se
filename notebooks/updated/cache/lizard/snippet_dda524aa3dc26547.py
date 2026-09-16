def _init_associations(fin_anno, taxid=None, taxids=None):
    return InitAssc(taxid, taxids).init_associations(fin_anno, taxids)