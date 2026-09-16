def evaluate_at(self, vals):
    new_vals = self._vals.copy()
    new_vals.update(vals)
    return self.__class__(self.operand, derivs=self._derivs, vals=new_vals)