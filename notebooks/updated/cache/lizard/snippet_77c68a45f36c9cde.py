def grant_access(src, dst='any', port=None, proto=None, index=None):
    return modify_access(src, dst=dst, port=port, proto=proto, action=
        'allow', index=index)