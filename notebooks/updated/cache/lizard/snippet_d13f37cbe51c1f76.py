def set_config(self, config):
    self.config.update(config)
    if self.config_map:
        for child_name in self.config_map:
            child_config = self._compound_children[child_name].get_config()
            for parent_item, child_item in self.config_map[child_name]:
                child_config[child_item] = self.config[parent_item]
            self._compound_children[child_name].set_config(child_config)
    else:
        for name, child in self._compound_children.items():
            child.set_config(self.config[name])