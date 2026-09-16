def make_params(self):
    if self.needs_dummy_fprop:
        if hasattr(self, '_dummy_input'):
            return
        self._dummy_input = self.make_input_placeholder()
        self.fprop(self._dummy_input)