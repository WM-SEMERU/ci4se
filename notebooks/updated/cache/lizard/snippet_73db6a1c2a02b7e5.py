def new_output_file_opt(self, opt, name):
    fil = File(name)
    self.add_output_opt(opt, fil)
    return fil