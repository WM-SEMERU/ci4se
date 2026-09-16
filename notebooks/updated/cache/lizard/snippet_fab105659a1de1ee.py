def write_config_json(config_file, data):
    outfile = None
    try:
        with open(config_file, 'w') as outfile:
            json.dump(data, outfile)
    except:
        line, filename, synerror = trace()
        raise ArcRestHelperError({'function': 'init_config_json', 'line':
            line, 'filename': filename, 'synerror': synerror})
    finally:
        outfile = None
        del outfile
        gc.collect()