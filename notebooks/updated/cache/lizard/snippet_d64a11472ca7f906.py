def allreduce_grads(self):
    if not self._kv_initialized:
        self._init_kvstore()
    if self._params_to_init:
        self._init_params()
    assert not (self._kvstore and self._update_on_kvstore
        ), 'allreduce_grads() when parameters are updated on kvstore is not supported. Try setting `update_on_kvstore` to False when creating trainer.'
    self._allreduce_grads()