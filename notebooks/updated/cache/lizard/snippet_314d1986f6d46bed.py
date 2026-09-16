def deserialize(data):
    try:
        module = import_module(data.get('class').get('module'))
        cls = getattr(module, data.get('class').get('name'))
    except ImportError:
        raise ImportError('No module named: %r' % data.get('class').get(
            'module'))
    except AttributeError:
        raise ImportError('module %r does not contain class %r' % (data.get
            ('class').get('module'), data.get('class').get('name')))
    class_params = cls.class_params(hidden=True)
    params = dict((name, class_params[name].deserialize(value)) for name,
        value in data.get('params').items())
    return cls(**params)