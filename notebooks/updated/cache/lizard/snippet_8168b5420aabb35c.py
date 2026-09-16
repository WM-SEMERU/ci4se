def GetOutputPluginStates(output_plugins, source=None, token=None):
    output_plugins_states = []
    for plugin_descriptor in output_plugins:
        plugin_class = plugin_descriptor.GetPluginClass()
        try:
            _, plugin_state = plugin_class.CreatePluginAndDefaultState(
                source_urn=source, args=plugin_descriptor.plugin_args,
                token=token)
        except Exception as e:
            raise ValueError('Plugin %s failed to initialize (%s)' % (
                plugin_class, e))
        plugin_state['logs'] = []
        plugin_state['errors'] = []
        output_plugins_states.append(rdf_flow_runner.OutputPluginState(
            plugin_state=plugin_state, plugin_descriptor=plugin_descriptor))
    return output_plugins_states