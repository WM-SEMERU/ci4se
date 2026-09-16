def fetch_option_taskfileinfos(self, typ, element):
    inter = self.get_typ_interface(typ)
    return inter.fetch_option_taskfileinfos(element)