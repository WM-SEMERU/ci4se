def load_object(s):
    try:
        m_path, o_name = s.rsplit('.', 1)
    except ValueError:
        raise ImportError('Cant import backend from path: {}'.format(s))
    module = import_module(m_path)
    return getattr(module, o_name)