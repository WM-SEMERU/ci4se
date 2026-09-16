def _input_handler_decorator(self, data):
    input_handler = getattr(self, self.__InputHandler)
    input_parts = [self.Parameters['taxonomy_file'], input_handler(data),
        self.Parameters['training_set_id'], self.Parameters[
        'taxonomy_version'], self.Parameters['modification_info'], self.
        ModelDir]
    return self._commandline_join(input_parts)