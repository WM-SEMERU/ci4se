def _load_income_model(self):
    self._add_model(self.income, self.state.income, IncomeModel)