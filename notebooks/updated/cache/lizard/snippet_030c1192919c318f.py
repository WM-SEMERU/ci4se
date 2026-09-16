def find_methods(self):
    methods = []
    req = self.request
    method_name = req.method.upper()
    method_names = set()
    members = inspect.getmembers(self)
    for member_name, member in members:
        if member_name.startswith(method_name):
            if member:
                methods.append((member_name, member))
                method_names.add(member_name)
    if len(methods) == 0:
        logger.warning('No methods to handle {} found'.format(method_name),
            exc_info=True)
        raise CallError(501, '{} {} not implemented'.format(req.method, req
            .path))
    elif len(methods) > 1 and method_name in method_names:
        raise ValueError(' '.join([
            'A multi method {} request should not have any methods named {}.',
            'Instead, all {} methods should use use an appropriate decorator',
            'like @route or @version and have a unique name starting with {}_'
            ]).format(method_name, method_name, method_name, method_name))
    return methods