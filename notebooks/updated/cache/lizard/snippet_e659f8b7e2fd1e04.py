def handle(self):
    mapreduce_name = self._get_required_param('name')
    mapper_input_reader_spec = self._get_required_param('mapper_input_reader')
    mapper_handler_spec = self._get_required_param('mapper_handler')
    mapper_output_writer_spec = self.request.get('mapper_output_writer')
    mapper_params = self._get_params('mapper_params_validator',
        'mapper_params.')
    params = self._get_params('params_validator', 'params.')
    mr_params = map_job.JobConfig._get_default_mr_params()
    mr_params.update(params)
    if 'queue_name' in mapper_params:
        mr_params['queue_name'] = mapper_params['queue_name']
    mapper_params['processing_rate'] = int(mapper_params.get(
        'processing_rate') or parameters.config.PROCESSING_RATE_PER_SEC)
    mapper_spec = model.MapperSpec(mapper_handler_spec,
        mapper_input_reader_spec, mapper_params, int(mapper_params.get(
        'shard_count', parameters.config.SHARD_COUNT)), output_writer_spec=
        mapper_output_writer_spec)
    mapreduce_id = self._start_map(mapreduce_name, mapper_spec, mr_params,
        queue_name=mr_params['queue_name'], _app=mapper_params.get('_app'))
    self.json_response['mapreduce_id'] = mapreduce_id