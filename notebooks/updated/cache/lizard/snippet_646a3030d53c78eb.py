def save_model(self, model_filename):
    line = 'save_{}|'.format(model_filename)
    self.vw_process.sendline(line)