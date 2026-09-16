def custom_environment(self, **kwargs):
    old_env = self.update_environment(**kwargs)
    try:
        yield
    finally:
        self.update_environment(**old_env)