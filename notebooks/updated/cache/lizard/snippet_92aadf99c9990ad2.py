def with_connection(func, self, *args, **argd):
    self.connection = self.get_connection()
    self.connection.last_used = time.time()
    self.connection.pre_call_hook(self, func)
    return func(self, *args, **argd)