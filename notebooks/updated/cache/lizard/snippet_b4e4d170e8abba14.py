def _get_reconciled_name_object(self, other):
    name = get_op_result_name(self, other)
    if self.name != name:
        return self._shallow_copy(name=name)
    return self