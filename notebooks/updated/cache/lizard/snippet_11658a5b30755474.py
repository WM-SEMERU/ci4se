def choice_doinst(self):
    if 'doinst.sh' in self.sbo_files.split():
        doinst_sh = ReadSBo(self.sbo_url).doinst('doinst.sh')
        fill = self.fill_pager(doinst_sh)
        self.pager(doinst_sh + fill)