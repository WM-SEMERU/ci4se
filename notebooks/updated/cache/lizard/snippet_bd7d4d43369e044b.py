def get_bindings_starting_with_keys(self, keys):

    def get():
        result = []
        for b in self.key_bindings:
            if len(keys) < len(b.keys):
                match = True
                for i, j in zip(b.keys, keys):
                    if i != j and i != Keys.Any:
                        match = False
                        break
                if match:
                    result.append(b)
        return result
    return self._get_bindings_starting_with_keys_cache.get(keys, get)