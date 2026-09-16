def put_all(self, map):
    check_not_none(map, "map can't be None")
    if not map:
        return ImmediateFuture(None)
    partition_service = self._client.partition_service
    partition_map = {}
    for key, value in six.iteritems(map):
        check_not_none(key, "key can't be None")
        check_not_none(value, "value can't be None")
        entry = self._to_data(key), self._to_data(value)
        partition_id = partition_service.get_partition_id(entry[0])
        try:
            partition_map[partition_id].append(entry)
        except KeyError:
            partition_map[partition_id] = [entry]
    futures = []
    for partition_id, entry_list in six.iteritems(partition_map):
        future = self._encode_invoke_on_partition(map_put_all_codec,
            partition_id, entries=dict(entry_list))
        futures.append(future)
    return combine_futures(*futures)