def exec_module(self, module):
    code = self.get_code(module.__name__)
    if code is None:
        raise ImportError(
            'cannot load module {!r} when get_code() returns None'.format(
            module.__name__))
    exec(code, module.__dict__)