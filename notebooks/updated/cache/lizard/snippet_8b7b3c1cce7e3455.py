def format_modified(self, modified, sep=' '):
    if modified is not None:
        return modified.strftime('%Y-%m-%d{0}%H:%M:%S.%fZ'.format(sep))
    return ''