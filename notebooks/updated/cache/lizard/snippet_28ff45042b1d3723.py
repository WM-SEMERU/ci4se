def parse_image_name(name):
    name = name or ''
    if '/' in name:
        repository, other = name.split('/')
    else:
        repository, other = None, name
    if ':' in other:
        name, version = other.split(':')
    else:
        name, version = other, 'latest'
    return repository, name, version