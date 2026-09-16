def is_typing_handler(stream):
    while True:
        packet = yield from stream.get()
        session_id = packet.get('session_key')
        user_opponent = packet.get('username')
        typing = packet.get('typing')
        if session_id and user_opponent and typing is not None:
            user_owner = get_user_from_session(session_id)
            if user_owner:
                opponent_socket = ws_connections.get((user_opponent,
                    user_owner.username))
                if typing and opponent_socket:
                    yield from target_message(opponent_socket, {'type':
                        'opponent-typing', 'username': user_opponent})
            else:
                pass
        else:
            pass