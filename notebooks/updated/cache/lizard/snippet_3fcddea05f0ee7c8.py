def _lookup_vpc_allocs(query_type, session=None, order=None, **bfilter):
    if session is None:
        session = bc.get_reader_session()
    if order:
        query_method = getattr(session.query(nexus_models_v2.NexusVPCAlloc)
            .filter_by(**bfilter).order_by(order), query_type)
    else:
        query_method = getattr(session.query(nexus_models_v2.NexusVPCAlloc)
            .filter_by(**bfilter), query_type)
    try:
        vpcs = query_method()
        if vpcs:
            return vpcs
    except sa_exc.NoResultFound:
        pass
    raise c_exc.NexusVPCAllocNotFound(**bfilter)