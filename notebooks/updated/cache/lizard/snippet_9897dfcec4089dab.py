def record_action(self, method_name, *args, **kwargs):
    self.actions.append((method_name, args, kwargs))