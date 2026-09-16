def context(self, mapping_class=DotDictWithAcquisition):
    config = None
    try:
        config = self.get_config(mapping_class=mapping_class)
        yield config
    finally:
        if config:
            self._walk_and_close(config)