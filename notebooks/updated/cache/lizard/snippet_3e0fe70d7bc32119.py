def construct(self, window_dim, stride=1, fill_value=dtypes.NA):
    from .dataarray import DataArray
    window = self.obj.variable.rolling_window(self.dim, self.window,
        window_dim, self.center, fill_value=fill_value)
    result = DataArray(window, dims=self.obj.dims + (window_dim,), coords=
        self.obj.coords)
    return result.isel(**{self.dim: slice(None, None, stride)})