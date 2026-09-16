def get_platform_node_selector(self, platform):
    nodeselector = {}
    if platform:
        nodeselector_str = self._get_value('node_selector.' + platform,
            self.conf_section, 'node_selector.' + platform)
        nodeselector = self.generate_nodeselector_dict(nodeselector_str)
    return nodeselector