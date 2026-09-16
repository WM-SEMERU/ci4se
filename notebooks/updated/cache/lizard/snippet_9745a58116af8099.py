def call(self, method, *args):
    return self.begin_call(method, *args).result(self.timeout)