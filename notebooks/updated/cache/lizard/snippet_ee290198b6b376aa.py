def get_input_grads(self, merge_multi_context=True):
    assert self.binded and self.params_initialized and self.inputs_need_grad
    return self._curr_module.get_input_grads(merge_multi_context=
        merge_multi_context)