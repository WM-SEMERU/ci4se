def read_from(self, provider, null_allowed=False, **options):
    if self._data is None:
        pass
    elif is_provider(provider):
        if self._value < 0:
            pass
        elif null_allowed or self._value > 0:
            while True:
                self.bytestream = provider.read(self.address, self.data_size)
                index = self.deserialize_data()
                if index.bit != 0:
                    length = index.byte, index.bit
                    raise ContainerLengthError(self, length)
                if not index.update:
                    break
            if is_mixin(self._data) and get_nested(options):
                self._data.read_from(provider, **options)
        else:
            self.bytestream = bytes()
            self.deserialize_data()
    else:
        raise ProviderTypeError(self, provider)