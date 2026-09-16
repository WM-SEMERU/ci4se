def check_data(self, ds, name, dims):
    if isinstance(name, six.string_types):
        name = [name]
        dims = [dims]
    else:
        dims = list(dims)
    variables = [ds[safe_list(n)[0]] for n in name]
    decoders = [CFDecoder.get_decoder(ds, var) for var in variables]
    default_slice = slice(None
        ) if self._default_slice is None else self._default_slice
    for i, (dim_dict, var, decoder) in enumerate(zip(dims, variables, decoders)
        ):
        corrected = decoder.correct_dims(var, dict(chain(six.iteritems(self
            ._default_dims), dim_dict.items())))
        for dim in var.dims:
            corrected.setdefault(dim, default_slice)
        dims[i] = [dim for dim, val in map(lambda t: (t[0], safe_list(t[1])
            ), six.iteritems(corrected)) if val and (len(val) > 1 or
            _is_slice(val[0]))]
    return self.plotter_cls.check_data(name, dims, [decoder.is_unstructured
        (var) for decoder, var in zip(decoders, variables)])