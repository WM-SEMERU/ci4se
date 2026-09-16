def _get_mapper_params(self):
    reader_params = self.input_reader_cls.params_to_json(self.
        input_reader_params)
    return {'input_reader': reader_params, 'output_writer': self.
        output_writer_params}