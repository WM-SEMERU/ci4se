def get_component_types(topic_id, remoteci_id, db_conn=None):
    db_conn = db_conn or flask.g.db_conn
    rconfiguration = remotecis.get_remoteci_configuration(topic_id,
        remoteci_id, db_conn=db_conn)
    if rconfiguration is not None and rconfiguration['component_types'
        ] is not None:
        component_types = rconfiguration['component_types']
    else:
        component_types = get_component_types_from_topic(topic_id, db_conn=
            db_conn)
    return component_types, rconfiguration