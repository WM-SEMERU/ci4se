def _get_node_dir(node):
    path = os.path.abspath(node)
    return path if os.path.isdir(path) else os.path.dirname(path)