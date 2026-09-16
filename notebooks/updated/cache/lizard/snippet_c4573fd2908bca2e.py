def async_update(self, event):
    self.update_attr(event.get('state', {}))
    super().async_update(event)