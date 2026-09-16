def instance_provisioned(device_id):
    session = db.get_reader_session()
    with session.begin():
        port_model = models_v2.Port
        res = bool(session.query(port_model).filter(port_model.device_id ==
            device_id).count())
    return res