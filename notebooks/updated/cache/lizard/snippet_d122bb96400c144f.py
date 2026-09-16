def ProcessRepliesWithOutputPlugins(self, replies):
    for output_plugin_state in self.context.output_plugins_states:
        plugin_descriptor = output_plugin_state.plugin_descriptor
        output_plugin_cls = plugin_descriptor.GetPluginClass()
        output_plugin = output_plugin_cls(source_urn=self.flow_obj.urn,
            args=plugin_descriptor.plugin_args, token=self.token)
        self.flow_obj.HeartBeat()
        try:
            output_plugin.ProcessResponses(output_plugin_state.plugin_state,
                replies)
            output_plugin.Flush(output_plugin_state.plugin_state)
            output_plugin.UpdateState(output_plugin_state.plugin_state)
            log_item = output_plugin_lib.OutputPluginBatchProcessingStatus(
                plugin_descriptor=plugin_descriptor, status='SUCCESS',
                batch_size=len(replies))
            output_plugin_state.Log(log_item)
            self.Log('Plugin %s successfully processed %d flow replies.',
                plugin_descriptor, len(replies))
        except Exception as e:
            error = output_plugin_lib.OutputPluginBatchProcessingStatus(
                plugin_descriptor=plugin_descriptor, status='ERROR',
                summary=utils.SmartUnicode(e), batch_size=len(replies))
            output_plugin_state.Error(error)
            self.Log('Plugin %s failed to process %d replies due to: %s',
                plugin_descriptor, len(replies), e)