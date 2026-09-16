def ua_string(praw_info):
    if os.environ.get('SERVER_SOFTWARE') is not None:
        info = os.environ.get('SERVER_SOFTWARE')
    else:
        info = platform.platform(True).encode('ascii', 'ignore')
    return '{0} PRAW/{1} Python/{2} {3}'.format(praw_info, __version__, sys
        .version.split()[0], info)