def _create_lua_method(self, name, code):
    script = self.register_script(code)
    setattr(script, 'name', name)
    method = lambda key, *a, **k: script(keys=[key], args=a, **k)
    setattr(self, name, method)