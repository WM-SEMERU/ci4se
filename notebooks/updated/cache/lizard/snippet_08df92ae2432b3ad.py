def split_filename(filename):
    if filename.endswith('.rpm'):
        filename = filename.split('.rpm')[0]
    components = filename.split(':')
    if len(components) > 1:
        epoch = components[0]
    else:
        epoch = ''
    arch = filename.rsplit('.')[-1]
    remaining = filename.rsplit('.%s' % arch)[0]
    release = remaining.rsplit('-')[-1]
    version = remaining.rsplit('-')[-2]
    name = '-'.join(remaining.rsplit('-')[:-2])
    return name, version, release, epoch, arch