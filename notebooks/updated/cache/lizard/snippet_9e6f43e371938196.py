def list_plugins():
    plugin_eps = pkg_resources.iter_entry_points('ofxstatement')
    return sorted((ep.name, ep.load()) for ep in plugin_eps)