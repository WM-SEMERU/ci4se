def get_go2nt(self, usr_go2nt):
    gos_all = self.get_gos_all()
    prt_flds_all = get_hdridx_flds() + self.gosubdag.prt_attr['flds']
    if not usr_go2nt:
        return self.__init_go2nt_dflt(gos_all, prt_flds_all)
    usr_nt_flds = next(iter(usr_go2nt.values()))._fields
    if len(set(prt_flds_all).difference(usr_nt_flds)) == 0:
        return self._init_go2nt_aug(usr_go2nt)
    return self.__init_go2nt_w_usr(gos_all, usr_go2nt, prt_flds_all)