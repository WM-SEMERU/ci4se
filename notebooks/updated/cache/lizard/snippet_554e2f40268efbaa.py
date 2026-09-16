def save_file(path, data, readable=False):
    if not path:
        IOError('No path specified to save')
    try:
        with io.open(path, 'w', encoding='utf-8') as f:
            if path.endswith('.json'):
                save_json_file(f, data, pretty=readable, compact=not
                    readable, sort=True)
            elif path.endswith('.yaml') or path.endswith('.yml'):
                save_yaml_file(f, data)
    except IOError:
        raise
    except Exception as e:
        raise IOError(e)