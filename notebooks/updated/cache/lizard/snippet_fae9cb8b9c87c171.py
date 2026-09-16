def set_model_pathnames(self):
    self.control_path = self.expt.control_path
    self.input_basepath = self.expt.lab.input_basepath
    self.work_path = self.expt.work_path
    self.codebase_path = self.expt.lab.codebase_path
    if len(self.expt.models) > 1:
        self.control_path = os.path.join(self.control_path, self.name)
        self.work_path = os.path.join(self.work_path, self.name)
        self.codebase_path = os.path.join(self.codebase_path, self.name)
    self.work_input_path = self.work_path
    self.work_restart_path = self.work_path
    self.work_output_path = self.work_path
    self.work_init_path = self.work_path
    self.exec_prefix = self.config.get('exe_prefix', '')
    self.exec_name = self.config.get('exe', self.default_exec)
    if self.exec_name:
        self.exec_path = os.path.join(self.expt.lab.bin_path, self.exec_name)
    else:
        self.exec_path = None
    if self.exec_path:
        self.exec_name = os.path.basename(self.exec_path)