def get_diff(a, b, *args, **kwargs):
    encoding = 'utf-8', 'latin-1', __salt_system_encoding__
    import salt.utils.data
    return ''.join(difflib.unified_diff(salt.utils.data.decode_list(a,
        encoding=encoding), salt.utils.data.decode_list(b, encoding=
        encoding), *args, **kwargs))