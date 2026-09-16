def init_config(self):
    input_fpath = os.path.join(self.work_path, 'input.nml')
    input_nml = f90nml.read(input_fpath)
    if self.expt.counter == 0 or self.expt.repeat_run:
        input_type = 'n'
    else:
        input_type = 'r'
    input_nml['MOM_input_nml']['input_filename'] = input_type
    f90nml.write(input_nml, input_fpath, force=True)