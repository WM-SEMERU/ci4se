def delete_cell(self, key):
    try:
        self.code_array.pop(key)
    except KeyError:
        pass
    self.grid.code_array.result_cache.clear()