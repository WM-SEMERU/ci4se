def _add_to_stack(self, item, value):
    p_value = item, value
    if p_value not in self.stack:
        self.stack.append(p_value)