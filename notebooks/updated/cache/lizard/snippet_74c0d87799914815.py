def build_backend(self, backend_node):
    proxy_name = backend_node.backend_header.proxy_name.text
    config_block_lines = self.__build_config_block(backend_node.config_block)
    return config.Backend(name=proxy_name, config_block=config_block_lines)