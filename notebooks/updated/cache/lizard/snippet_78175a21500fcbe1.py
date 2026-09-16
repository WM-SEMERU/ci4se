def auto_code_block(self, *args, **kwargs):
    self.stored_nested_parse = self.state_machine.state.nested_parse
    self.state_machine.state.nested_parse = self.patched_nested_parse
    try:
        return super(PatchedAutoStructify, self).auto_code_block(*args, **
            kwargs)
    finally:
        self.state_machine.state.nested_parse = self.stored_nested_parse