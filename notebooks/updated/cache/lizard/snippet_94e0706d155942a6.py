def _lookup_vpc_count_min_max(session=None, **bfilter):
    if session is None:
        session = bc.get_reader_session()
    try:
        res = session.query(func.count(nexus_models_v2.NexusVPCAlloc.vpc_id
            ), func.min(nexus_models_v2.NexusVPCAlloc.vpc_id), func.max(
            nexus_models_v2.NexusVPCAlloc.vpc_id)).filter(nexus_models_v2.
            NexusVPCAlloc.switch_ip == bfilter['switch_ip']).one()
        count = res[0]
        sw_min = res[1]
        sw_max = res[2]
        return count, sw_min, sw_max
    except sa_exc.NoResultFound:
        pass
    raise c_exc.NexusVPCAllocNotFound(**bfilter)