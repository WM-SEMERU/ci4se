def sync_node(node):
    if node.get('dummy') or 'dummy' in node.get('tags', []):
        lib.print_header('Skipping dummy: {0}'.format(env.host))
        return False
    current_node = lib.get_node(node['name'])
    solo.configure(current_node)
    ipaddress = _get_ipaddress(node)
    filepath = save_config(node, ipaddress)
    try:
        _synchronize_node(filepath, node)
        _configure_node()
    finally:
        _node_cleanup()
    return True