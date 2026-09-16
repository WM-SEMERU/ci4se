def _validate_node(self, node):
    c = Composer(self.device, node)
    if c.schema_node is None:
        p = self.device.get_xpath(node, instance=False)
        raise ConfigError('schema node of the config node not found: {}'.
            format(p))
    if c.schema_node.get('type') == 'list':
        for key in c.keys:
            if node.find(key) is None:
                p = self.device.get_xpath(node, instance=False)
                raise ConfigError("missing key '{}' of the config node {}".
                    format(key, p))
    for tag in (operation_tag, insert_tag, value_tag, key_tag):
        if node.get(tag):
            raise ConfigError(
                "the config node contains invalid attribute '{}': {}".
                format(tag, self.device.get_xpath(node)))
    for child in node.getchildren():
        if len(child) > 0:
            self._validate_node(child)
        child_schema_node = self.device.get_schema_node(child)
        if child_schema_node is None:
            raise ConfigError(
                'schema node of the config node {} cannot be found:\n{}'.
                format(self.device.get_xpath(child), self))
        if len(child) == 0 and child_schema_node.get('type'
            ) == 'container' and child_schema_node.get('presence') != 'true':
            node.remove(child)