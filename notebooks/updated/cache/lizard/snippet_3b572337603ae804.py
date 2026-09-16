def _obtain_sampled_health_pills(self, run, node_names):
    runs_to_tags_to_content = self._event_multiplexer.PluginRunToTagToContent(
        constants.DEBUGGER_PLUGIN_NAME)
    if run not in runs_to_tags_to_content:
        return {}
    tags_to_content = runs_to_tags_to_content[run]
    mapping = {}
    for node_name in node_names:
        if node_name not in tags_to_content:
            continue
        health_pills = []
        for tensor_event in self._event_multiplexer.Tensors(run, node_name):
            json_string = tags_to_content[node_name]
            try:
                content_object = json.loads(tf.compat.as_text(json_string))
                device_name = content_object['device']
                output_slot = content_object['outputSlot']
                health_pills.append(self._tensor_proto_to_health_pill(
                    tensor_event, node_name, device_name, output_slot))
            except (KeyError, ValueError) as e:
                logger.error(
                    'Could not determine device from JSON string %r: %r',
                    json_string, e)
        mapping[node_name] = health_pills
    return mapping