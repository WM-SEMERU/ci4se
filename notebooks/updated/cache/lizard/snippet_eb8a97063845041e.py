def json_loads(inbox):
    gc.disable()
    obj = json.loads(inbox[0])
    gc.enable()
    return obj