def get_partition_offsets(self, topic, partition, request_time_ms,
    max_num_offsets):
    reqs = [OffsetRequest(topic, partition, request_time_ms, max_num_offsets)]
    resp, = self._client.send_offset_request(reqs)
    check_error(resp)
    assert resp.topic == topic
    assert resp.partition == partition
    return resp.offsets