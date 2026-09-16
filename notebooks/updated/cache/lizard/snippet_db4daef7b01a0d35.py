def setup_list_pars(self):
    tdf = self.setup_temporal_list_pars()
    sdf = self.setup_spatial_list_pars()
    if tdf is None and sdf is None:
        return
    os.chdir(self.m.model_ws)
    try:
        apply_list_pars()
    except Exception as e:
        os.chdir('..')
        self.logger.lraise('error test running apply_list_pars():{0}'.
            format(str(e)))
    os.chdir('..')
    line = 'pyemu.helpers.apply_list_pars()\n'
    self.logger.statement('forward_run line:{0}'.format(line))
    self.frun_pre_lines.append(line)