def check_config(self):
    cfg_error_msg = (
        'PYMAGICC is not the only tuning model that will be used by `MAGCFG_USER.CFG`: your run is likely to fail/do odd things'
        )
    emisscen_error_msg = (
        "You have more than one `FILE_EMISSCEN_X` flag set. Using more than one emissions scenario is hard to debug and unnecessary with Pymagicc's dataframe scenario input. Please combine all your scenarios into one dataframe with Pymagicc and pandas, then feed this single Dataframe into Pymagicc's run API."
        )
    nml_to_check = 'nml_allcfgs'
    usr_cfg = read_cfg_file(join(self.run_dir, 'MAGCFG_USER.CFG'))
    for k in usr_cfg[nml_to_check]:
        if k.startswith('file_tuningmodel'):
            first_tuningmodel = k in ['file_tuningmodel', 'file_tuningmodel_1']
            if first_tuningmodel:
                if usr_cfg[nml_to_check][k] != 'PYMAGICC':
                    raise ValueError(cfg_error_msg)
            elif usr_cfg[nml_to_check][k] not in ['USER', '']:
                raise ValueError(cfg_error_msg)
        elif k.startswith('file_emisscen_'):
            if usr_cfg[nml_to_check][k] not in ['NONE', '']:
                raise ValueError(emisscen_error_msg)