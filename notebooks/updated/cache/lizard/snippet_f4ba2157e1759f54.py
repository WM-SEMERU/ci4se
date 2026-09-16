def _install_node(self):
    node_package_path = self.select()
    node_bin_path = os.path.join(node_package_path, 'node', 'bin')
    if not is_readable_dir(node_bin_path):
        return os.path.join(node_package_path, os.listdir(node_package_path
            )[0], 'bin')
    return node_bin_path