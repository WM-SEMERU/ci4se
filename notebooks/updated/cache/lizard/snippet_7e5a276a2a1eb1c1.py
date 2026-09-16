def _add_plugin_paths(self):
    base_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    ansible_mitogen.loaders.connection_loader.add_directory(os.path.join(
        base_dir, 'connection'))
    ansible_mitogen.loaders.action_loader.add_directory(os.path.join(
        base_dir, 'action'))