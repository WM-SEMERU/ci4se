def spawn_watcher(self, label, target=None, eternal=False):
    if label not in self._sources:
        raise YapconfSourceError('Cannot watch %s no source named %s' % (
            label, label))
    current_config = self._sources[label].get_data()
    handler = ConfigChangeHandler(current_config, self, target)
    return self._sources[label].watch(handler, eternal)