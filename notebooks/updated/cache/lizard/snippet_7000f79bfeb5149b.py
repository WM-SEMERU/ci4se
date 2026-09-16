def delete_consumer_group(self, project, logstore, consumer_group):
    headers = {'x-log-bodyrawsize': '0'}
    params = {}
    resource = '/logstores/' + logstore + '/consumergroups/' + consumer_group
    resp, header = self._send('DELETE', project, None, resource, params,
        headers)
    return DeleteConsumerGroupResponse(header, resp)