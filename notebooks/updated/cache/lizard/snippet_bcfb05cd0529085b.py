def is_exception(node):
    if node.name in ('Exception', 'BaseException') and node.root(
        ).name == _EXCEPTIONS_MODULE:
        return True
    if not hasattr(node, 'ancestors'):
        return False
    return any(is_exception(parent) for parent in node.ancestors(recurs=True))