def get_params_from_kv(self, arg_params, aux_params):
    assert self._kvstore is not None
    for name, block in zip(self._exec_group.param_names, self._exec_group.
        param_arrays):
        assert isinstance(block, list)
        if block[0].stype == 'row_sparse':
            row_ids = mx.nd.arange(start=0, stop=block[0].shape[0], dtype=
                'int64')
            self._kvstore.row_sparse_pull(name, arg_params[name], row_ids=
                row_ids)
        else:
            assert block[0].stype == 'default'
            self._kvstore.pull(name, out=arg_params[name])
    if len(aux_params) > 0:
        raise NotImplementedError()
    return arg_params, aux_params