def _prepare_transforms(self):
    for offset, value in enumerate(self._config.get(config.TRANSFORMS, [])):
        self._config[config.TRANSFORMS][offset] = self._import_class(value)