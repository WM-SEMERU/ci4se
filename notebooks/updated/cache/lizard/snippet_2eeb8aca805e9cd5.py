def get_config_node(self):
    default_ns = ''
    config_node = etree.Element(config_tag, nsmap={'nc': nc_url})
    for index, url_piece in enumerate(self._url_pieces):
        if index == len(self._url_pieces) - 1:
            config_node_parent = self.copy(config_node)
        node_name, values = self.parse_url_piece(url_piece)
        default_ns, tag = self.convert_tag(default_ns, node_name, src=Tag.
            JSON_NAME, dst=Tag.LXML_ETREE)
        config_node = self.subelement(config_node, tag, None)
        schema_node = self.device.get_schema_node(config_node)
        if schema_node.get('type') == 'leaf-list' and len(values) > 0:
            model_name, text_value = self.get_name(values[0])
            if model_name:
                prefix = self._name_to_prefix[model_name]
                config_node.text = '{}:{}'.format(prefix, text_value)
            else:
                config_node.text = text_value
        elif schema_node.get('type') == 'list' and len(values) > 0:
            key_tags = BaseCalculator._get_list_keys(schema_node)
            for key_tag, value in zip(key_tags, values):
                key = self.subelement(config_node, key_tag, value)
    return config_node_parent, config_node