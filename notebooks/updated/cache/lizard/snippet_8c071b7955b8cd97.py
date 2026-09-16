def get_docs_url(self, role, name):
    if role == 'cite':
        if name not in self.env.bibtex_cache.get_all_cited_keys():
            raise KeyError('cite key %s not found' % name, 'cite', 0)
        url = self.baseurl + 'zreferences.html#' + name
    elif role == 'ref':
        try:
            reftpl = self.env.domaindata['std']['labels'][name]
        except Exception:
            raise KeyError('ref label %s not found' % name, 'ref', 0)
        url = self.baseurl + reftpl[0] + '.html#' + reftpl[1]
    else:
        url = None
        for ii in self.invlst:
            try:
                url = ii.get_docs_url(role, name)
            except KeyError as ex:
                if ex.args[1] == 'role' or ex.args[2] > 1:
                    raise ex
            else:
                break
        if url is None:
            raise KeyError('name %s not found' % name, 'name', 0)
    return url