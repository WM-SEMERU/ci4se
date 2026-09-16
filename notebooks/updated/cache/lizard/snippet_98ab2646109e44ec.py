def await_scene_loaded(cli, scene_name, is_loaded=DEFAULT_SCENE_LOADED,
    timeout_seconds=DEFAULT_TIMEOUT_SECONDS):
    message_payload = {'scene_name': scene_name, 'is_loaded': is_loaded,
        'timeout': timeout_seconds}
    msg = message.Message('await.unity.scene.loaded', message_payload)
    cli.send_message(msg)
    response = cli.read_message()
    verify_response(response)
    return bool(response['payload']['success'])