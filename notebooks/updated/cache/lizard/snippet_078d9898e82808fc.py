def get_cluster(dc_ref, cluster):
    dc_name = get_managed_object_name(dc_ref)
    log.trace("Retrieving cluster '%s' from datacenter '%s'", cluster, dc_name)
    si = get_service_instance_from_managed_object(dc_ref, name=dc_name)
    traversal_spec = vmodl.query.PropertyCollector.TraversalSpec(path=
        'hostFolder', skip=True, type=vim.Datacenter, selectSet=[vmodl.
        query.PropertyCollector.TraversalSpec(path='childEntity', skip=
        False, type=vim.Folder)])
    items = [i['object'] for i in get_mors_with_properties(si, vim.
        ClusterComputeResource, container_ref=dc_ref, property_list=['name'
        ], traversal_spec=traversal_spec) if i['name'] == cluster]
    if not items:
        raise salt.exceptions.VMwareObjectRetrievalError(
            "Cluster '{0}' was not found in datacenter '{1}'".format(
            cluster, dc_name))
    return items[0]