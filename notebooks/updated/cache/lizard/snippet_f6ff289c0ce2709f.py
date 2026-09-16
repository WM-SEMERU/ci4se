def FailoverInstance(r, instance, iallocator=None, ignore_consistency=False,
    target_node=None):
    body = {'ignore_consistency': ignore_consistency}
    if iallocator is not None:
        body['iallocator'] = iallocator
    if target_node is not None:
        body['target_node'] = target_node
    return r.request('put', '/2/instances/%s/failover' % instance, content=body
        )