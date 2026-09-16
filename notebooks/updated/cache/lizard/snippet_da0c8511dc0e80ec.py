def get_indelcaller(d_or_c):
    config = d_or_c if isinstance(d_or_c, dict
        ) and 'config' in d_or_c else d_or_c
    indelcaller = config['algorithm'].get('indelcaller', '')
    if not indelcaller:
        indelcaller = ''
    if isinstance(indelcaller, (list, tuple)):
        indelcaller = indelcaller[0] if len(indelcaller) > 0 else ''
    return indelcaller