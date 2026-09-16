def set_metadata(self, loadbalancer, metadata, node=None):
    self.delete_metadata(loadbalancer, node=node)
    metadata_list = [{'key': key, 'value': val} for key, val in metadata.
        items()]
    if node:
        uri = '/loadbalancers/%s/nodes/%s/metadata' % (utils.get_id(
            loadbalancer), utils.get_id(node))
    else:
        uri = '/loadbalancers/%s/metadata' % utils.get_id(loadbalancer)
    req_body = {'metadata': metadata_list}
    resp, body = self.api.method_post(uri, body=req_body)
    return body