def _request(self):
    caller_frame = inspect.getouterframes(inspect.currentframe())[1]
    args, _, _, values = inspect.getargvalues(caller_frame[0])
    caller_name = caller_frame[3]
    kwargs = {arg: values[arg] for arg in args if arg != 'self'}
    func = reduce(lambda resource, name: resource.__getattr__(name), self.
        mappings[caller_name].split('.'), self)
    return func(**kwargs)