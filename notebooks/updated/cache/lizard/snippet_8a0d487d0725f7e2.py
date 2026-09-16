def _classnamedict(self, classname, namespace):
    clns = self._classnamelist(classname, namespace)
    rtn_dict = NocaseDict()
    for cln in clns:
        rtn_dict[cln] = cln
    return rtn_dict