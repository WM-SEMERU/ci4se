def cache_script(script, text, opts={}):
    global script_cache
    if script not in script_cache:
        update_script_cache(script, text, opts)
        pass
    return script