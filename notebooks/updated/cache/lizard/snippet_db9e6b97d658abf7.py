def eval(self, command):
    if self.logger.handlers:
        self.logger.debug(command.decode('utf-8'))
    if self.tcl_script:
        self.tcl_script.info(command)
    self.rc = self.tcl_interp.eval(command)
    if self.logger.handlers:
        self.logger.debug('\t' + self.rc.decode('utf-8'))
    return self.rc