def minimum_needs(self, input_layer):
    output_layer = self.prepare_new_layer(input_layer)
    for needs in minimum_needs_post_processors:
        is_success, message = run_single_post_processor(output_layer, needs)
        if not is_success:
            LOGGER.debug(message)
            display_critical_message_box(title=self.tr(
                'Error while running post processor'), message=message)
            return False, None
    return True, output_layer