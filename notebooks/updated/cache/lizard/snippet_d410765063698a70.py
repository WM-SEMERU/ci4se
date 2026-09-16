def clear_globals_reload_modules(self):
    self.code_array.clear_globals()
    self.code_array.reload_modules()
    self.code_array.result_cache.clear()