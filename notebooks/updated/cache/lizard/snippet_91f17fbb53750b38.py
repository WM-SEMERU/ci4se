def register(self, dtype):
    if not issubclass(dtype, (PandasExtensionDtype, ExtensionDtype)):
        raise ValueError('can only register pandas extension dtypes')
    self.dtypes.append(dtype)