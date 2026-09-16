def parametrize_grid(self, debug=False):
    self.set_voltage_level()
    self._station.set_operation_voltage_level()
    (self.default_branch_type, self.default_branch_type_aggregated, self.
        default_branch_type_settle) = self.set_default_branch_type(debug)
    self.default_branch_kind_aggregated = self.default_branch_kind
    self.default_branch_kind_settle = 'cable'
    self._station.select_transformers()