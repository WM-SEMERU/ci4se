def post_process(self, layer):
    LOGGER.info('ANALYSIS : Post processing')
    purpose = layer.keywords['layer_purpose']
    if purpose != layer_purpose_aggregation_summary['key']:
        layer_title(layer)
    for post_processor in post_processors:
        run, run_message = should_run(layer.keywords, post_processor)
        if run:
            valid, message = enough_input(layer, post_processor['input'])
            name = post_processor['name']
            if valid:
                valid, message = run_single_post_processor(layer,
                    post_processor)
                if valid:
                    self.set_state_process('post_processor', name)
                    message = '{name} : Running'.format(name=name)
                    LOGGER.info(message)
            else:
                pass
        else:
            pass
    self.debug_layer(layer, add_to_datastore=False)