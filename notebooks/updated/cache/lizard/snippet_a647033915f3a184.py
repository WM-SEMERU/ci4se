def find_module(fdr, fqname, path=None):
    if fqname in fdr.aliases:
        return Loader(fqname, fdr.aliases[fqname])
    return None