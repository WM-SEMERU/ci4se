def execute_on_key_owner(self, key, task):
    check_not_none(key, "key can't be None")
    key_data = self._to_data(key)
    partition_id = self._client.partition_service.get_partition_id(key_data)
    uuid = self._get_uuid()
    return self._encode_invoke_on_partition(
        executor_service_submit_to_partition_codec, partition_id, uuid=uuid,
        callable=self._to_data(task), partition_id=partition_id)