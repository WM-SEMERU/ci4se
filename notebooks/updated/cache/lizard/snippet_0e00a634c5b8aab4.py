def build_on_entry(self, runnable, regime, on_entry):
    on_entry_code = []
    on_entry_code += ['if self.current_regime != self.last_regime:']
    on_entry_code += ['    self.last_regime = self.current_regime']
    for action in on_entry.actions:
        code = self.build_action(runnable, regime, action)
        for line in code:
            on_entry_code += ['    ' + line]
    return on_entry_code