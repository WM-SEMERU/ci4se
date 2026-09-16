def change_class(self):
    self.toolbarcenterframe.config(text='Draw: {}'.format(self.config.
        solar_class_name[self.solar_class_var.get()]))