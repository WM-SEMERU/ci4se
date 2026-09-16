def _get_input_readers(self, state):
    serialized_input_readers_key = (self._SERIALIZED_INPUT_READERS_KEY %
        state.key().id_or_name())
    serialized_input_readers = model._HugeTaskPayload.get_by_key_name(
        serialized_input_readers_key, parent=state)
    input_reader_class = state.mapreduce_spec.mapper.input_reader_class()
    split_param = state.mapreduce_spec.mapper
    if issubclass(input_reader_class, map_job.InputReader):
        split_param = map_job.JobConfig._to_map_job_config(state.
            mapreduce_spec, os.environ.get('HTTP_X_APPENGINE_QUEUENAME'))
    if serialized_input_readers is None:
        readers = input_reader_class.split_input(split_param)
    else:
        readers = [input_reader_class.from_json_str(_json) for _json in
            json.loads(zlib.decompress(serialized_input_readers.payload))]
    if not readers:
        return None, None
    state.mapreduce_spec.mapper.shard_count = len(readers)
    state.active_shards = len(readers)
    if serialized_input_readers is None:
        serialized_input_readers = model._HugeTaskPayload(key_name=
            serialized_input_readers_key, parent=state)
        readers_json_str = [i.to_json_str() for i in readers]
        serialized_input_readers.payload = zlib.compress(json.dumps(
            readers_json_str))
    return readers, serialized_input_readers