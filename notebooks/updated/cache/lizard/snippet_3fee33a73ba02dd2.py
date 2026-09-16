def yaml_block(self):
    if LOAD_YAML and self._yaml_block is not None:
        try:
            yaml_dict = yaml.load(self._yaml_block)
            return yaml_dict
        except yaml.error.YAMLError:
            print('Error parsing yaml block. Check formatting.')
    return None