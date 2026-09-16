def save_cache(cache):
    with open(settings.DUP_FILTER_FILE, 'w') as f:
        f.write(json.dumps(list(cache)))