def put_values(self):
    for value_name, widget in self.index.items():
        widget.set_value(self.value[value_name])
        widget.connect(self.set_modified)