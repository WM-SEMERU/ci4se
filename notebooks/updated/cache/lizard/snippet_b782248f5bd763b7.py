def restart(self):
    restart_file = None
    wfk_file = self.outdir.has_abiext('WFK')
    if False and wfk_file:
        irdvars = irdvars_for_ext('WFK')
        restart_file = self.out_to_in(wfk_file)
    if restart_file is None:
        for ext in ('', '.nc'):
            out_den = self.outdir.path_in('out_DEN' + ext)
            if os.path.exists(out_den):
                irdvars = irdvars_for_ext('DEN')
                restart_file = self.out_to_in(out_den)
                break
    if restart_file is None:
        last_timden = self.outdir.find_last_timden_file()
        if last_timden is not None:
            if last_timden.path.endswith('.nc'):
                ofile = self.outdir.path_in('out_DEN.nc')
            else:
                ofile = self.outdir.path_in('out_DEN')
            os.rename(last_timden.path, ofile)
            restart_file = self.out_to_in(ofile)
            irdvars = irdvars_for_ext('DEN')
    if restart_file is None:
        self.history.warning(
            'Cannot find the WFK|DEN|TIM?_DEN file to restart from.')
    else:
        self.set_vars(irdvars)
        self.history.info('Will restart from %s', restart_file)
    self._change_structure(self.get_final_structure())
    return self._restart()