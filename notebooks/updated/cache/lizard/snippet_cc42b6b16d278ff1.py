def remove(self, items):
    items = coerce_to_list(items)
    new_options = {k: v for k, v in self.options.items() if v not in items}
    self.widget.options = new_options
    self.widget.param.trigger('options')