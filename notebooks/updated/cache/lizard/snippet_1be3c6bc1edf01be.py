def observed_data_to_xarray(self):
    if self.observed is None:
        return None
    observed_data = {}
    if isinstance(self.observed, self.tf.Tensor):
        with self.tf.Session() as sess:
            vals = sess.run(self.observed, feed_dict=self.feed_dict)
    else:
        vals = self.observed
    if self.dims is None:
        dims = {}
    else:
        dims = self.dims
    name = 'obs'
    val_dims = dims.get(name)
    vals = np.atleast_1d(vals)
    val_dims, coords = generate_dims_coords(vals.shape, name, dims=val_dims,
        coords=self.coords)
    observed_data[name] = xr.DataArray(vals, dims=val_dims, coords=coords)
    return xr.Dataset(data_vars=observed_data, attrs=make_attrs(library=
        self.tfp))