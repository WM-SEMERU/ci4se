def run_worker(wname, data, engine_uuid_hex=None, **kwargs):
    if 'stop_on_halt' not in kwargs:
        kwargs['stop_on_halt'] = False
    if engine_uuid_hex:
        engine_uuid = uuid.UUID(hex=engine_uuid_hex)
        engine = WorkflowEngine.from_uuid(uuid=engine_uuid, **kwargs)
    else:
        engine = WorkflowEngine.with_name(wname, **kwargs)
        engine.save()
    objects = get_workflow_object_instances(data, engine)
    db.session.commit()
    engine.process(objects, **kwargs)
    return engine