def get_go2nt(self, goea_results):
    go2obj = self.objaartall.grprdflt.gosubdag.go2obj
    goea_nts = MgrNtGOEAs(goea_results).get_nts_strpval()
    return {go2obj[nt.GO].id: nt for nt in goea_nts if nt.GO in go2obj}