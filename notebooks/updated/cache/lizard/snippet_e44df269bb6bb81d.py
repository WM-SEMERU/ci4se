def get_builder(self, env):
    builder = getattr(env, self.__name__)
    self.initializer.apply_tools(env)
    builder = getattr(env, self.__name__)
    if builder is self:
        return None
    self.initializer.remove_methods(env)
    return builder