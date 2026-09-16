def find_plugin(value, key=DEFAULT_LOOKUP_KEY, conn=None):
    result = list(RPC.filter({key: value}).run(conn))
    return result