def handle_comm_opened(comm, msg):
    version = msg.get('metadata', {}).get('version', '')
    if version.split('.')[0] != PROTOCOL_VERSION_MAJOR:
        raise ValueError(
            'Incompatible widget protocol versions: received version %r, expected version %r'
             % (version, __protocol_version__))
    data = msg['content']['data']
    state = data['state']
    widget_class = Widget.widget_types.get(state['_model_module'], state[
        '_model_module_version'], state['_model_name'], state[
        '_view_module'], state['_view_module_version'], state['_view_name'])
    widget = widget_class(comm=comm)
    if 'buffer_paths' in data:
        _put_buffers(state, data['buffer_paths'], msg['buffers'])
    widget.set_state(state)