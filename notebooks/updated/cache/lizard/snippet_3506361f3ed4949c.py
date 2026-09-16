def _format_stack(self, stack, current=None):
    if current is not None:
        stack = stack + [current]
    if len(stack) > 1:
        prefix = os.path.commonprefix(stack)
        if prefix.endswith('/'):
            prefix = prefix[:-1]
        stack = [scope[len(prefix):] for scope in stack]
    return ' => '.join(stack)