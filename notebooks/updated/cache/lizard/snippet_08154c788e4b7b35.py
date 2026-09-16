def join_room(room, sid=None, namespace=None):
    socketio = flask.current_app.extensions['socketio']
    sid = sid or flask.request.sid
    namespace = namespace or flask.request.namespace
    socketio.server.enter_room(sid, room, namespace=namespace)