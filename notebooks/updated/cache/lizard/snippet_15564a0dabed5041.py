def pause(jid, state_id=None, duration=None):
    jid = six.text_type(jid)
    if state_id is None:
        state_id = '__all__'
    data, pause_path = _get_pause(jid, state_id)
    if duration:
        data[state_id]['duration'] = int(duration)
    with salt.utils.files.fopen(pause_path, 'wb') as fp_:
        fp_.write(salt.utils.msgpack.dumps(data))