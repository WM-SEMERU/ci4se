def find_replace(obj, find, replace):
    try:
        if isinstance(obj, dict):
            return {find_replace(key, find, replace): find_replace(value,
                find, replace) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [find_replace(element, find, replace) for element in obj]
        elif obj == find:
            return unicode_convert(replace)
        else:
            try:
                return unicode_convert(find_replace_string(obj, find, replace))
            except:
                return unicode_convert(obj)
    except:
        line, filename, synerror = trace()
        raise ArcRestHelperError({'function': 'find_replace', 'line': line,
            'filename': filename, 'synerror': synerror})
    finally:
        pass