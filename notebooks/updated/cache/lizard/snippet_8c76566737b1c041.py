def read_lua_file(dotted_module, path=None, context=None):
    path = path or DEFAULT_LUA_PATH
    bits = dotted_module.split('.')
    bits[-1] += '.lua'
    name = os.path.join(path, *bits)
    with open(name) as f:
        data = f.read()
    if context:
        data = data.format(context)
    return data