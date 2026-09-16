def set(self, value):
    old_value = self._value
    old_raw_str_value = self.raw_str_value
    self.type.set_item_value(self, value)
    new_value = self._value
    if old_value is not_set and new_value is not_set:
        return
    if self.section:
        self.section.dispatch_event(self.section.hooks.item_value_changed,
            item=self, old_value=old_value, new_value=new_value,
            old_raw_str_value=old_raw_str_value, new_raw_str_value=self.
            raw_str_value)