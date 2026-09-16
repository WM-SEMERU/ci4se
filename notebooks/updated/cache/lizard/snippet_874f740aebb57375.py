def forward(self, x, *args):
    if isinstance(x, NDArray):
        with x.context as ctx:
            if self._active:
                return self._call_cached_op(x, *args)
            try:
                params = {i: j.data(ctx) for i, j in self._reg_params.items()}
            except DeferredInitializationError:
                self._deferred_infer_shape(x, *args)
                for _, i in self.params.items():
                    i._finish_deferred_init()
                params = {i: j.data(ctx) for i, j in self._reg_params.items()}
            return self.hybrid_forward(ndarray, x, *args, **params)
    assert isinstance(x, Symbol
        ), 'HybridBlock requires the first argument to forward be either Symbol or NDArray, but got %s' % type(
        x)
    params = {i: j.var() for i, j in self._reg_params.items()}
    with self.name_scope():
        return self.hybrid_forward(symbol, x, *args, **params)