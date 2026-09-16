def split_shard(self, project_name, logstore_name, shardId, split_hash):
    headers = {}
    params = {'action': 'split', 'key': split_hash}
    resource = '/logstores/' + logstore_name + '/shards/' + str(shardId)
    resp, header = self._send('POST', project_name, None, resource, params,
        headers)
    return ListShardResponse(resp, header)