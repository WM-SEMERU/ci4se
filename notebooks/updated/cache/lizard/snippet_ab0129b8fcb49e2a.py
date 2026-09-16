def _find_experiment_tag(self):
    with self._experiment_from_tag_lock:
        if self._experiment_from_tag is None:
            mapping = self.multiplexer.PluginRunToTagToContent(metadata.
                PLUGIN_NAME)
            for tag_to_content in mapping.values():
                if metadata.EXPERIMENT_TAG in tag_to_content:
                    self._experiment_from_tag = (metadata.
                        parse_experiment_plugin_data(tag_to_content[
                        metadata.EXPERIMENT_TAG]))
                    break
    return self._experiment_from_tag