def add_host_mapping(host_id, nexus_ip, interface, ch_grp, is_static):
    LOG.debug('add_nexusport_binding() called')
    session = bc.get_writer_session()
    mapping = nexus_models_v2.NexusHostMapping(host_id=host_id, if_id=
        interface, switch_ip=nexus_ip, ch_grp=ch_grp, is_static=is_static)
    try:
        session.add(mapping)
        session.flush()
    except db_exc.DBDuplicateEntry:
        with excutils.save_and_reraise_exception() as ctxt:
            if is_static:
                ctxt.reraise = False
                LOG.debug(
                    'Duplicate static entry encountered host=%(host)s, if=%(if)s, ip=%(ip)s'
                    , {'host': host_id, 'if': interface, 'ip': nexus_ip})
    return mapping