def upsert_link(self, link, overwrite_ref=False):
    elink = self.__links.get(link.id_)
    if elink:
        if elink.ref is None or overwrite_ref and link.ref:
            elink.ref = link.ref
        if link._title is not None:
            elink.title = link._title
        return elink
    if not overwrite_ref:
        sym = self.__doc_db.get_symbol(link.id_)
        if sym and sym.link:
            self.__links[link.id_] = sym.link
            return sym.link
    self.add_link(link)
    return link