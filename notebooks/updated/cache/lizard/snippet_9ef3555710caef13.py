def show(self):
    self.show_info()
    self.show_notes()
    if self.code:
        self.each_params_by_register(self.code.get_registers_size(), self.
            get_descriptor())
        self.code.show()