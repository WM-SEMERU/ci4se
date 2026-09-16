def search_json_log(filepath, key, value):
    try:
        with open(filepath, 'r') as fh:
            for line in fh.readlines():
                log = json.loads(line)
                if key in log and log[key] == value:
                    return log
    except IOError:
        pass
    return False