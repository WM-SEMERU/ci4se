def get_title(src_name, src_type=None):
    if src_type == 'tcp':
        return '{0}:{1}'.format(*src_name)
    return os.path.basename(src_name)