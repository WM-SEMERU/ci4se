def records():
    with db.session.begin_nested():
        for idx in range(20):
            id_ = uuid.uuid4()
            Record.create({'title': 'LHC experiment {}'.format(idx),
                'description': 'Data from experiment {}.'.format(idx),
                'type': 'data', 'recid': idx}, id_=id_)
            PersistentIdentifier.create(pid_type='recid', pid_value=idx,
                object_type='rec', object_uuid=id_, status=PIDStatus.REGISTERED
                )
    db.session.commit()