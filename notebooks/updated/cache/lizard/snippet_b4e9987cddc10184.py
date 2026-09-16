def transform_cur_commands_interactive(_, **kwargs):
    event_payload = kwargs.get('event_payload', {})
    cur_commands = event_payload.get('text', '').split(' ')
    _transform_cur_commands(cur_commands)
    event_payload.update({'text': ' '.join(cur_commands)})