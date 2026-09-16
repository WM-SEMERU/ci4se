def ppa(state, host, name, present=True):
    if present:
        yield 'apt-add-repository -y "{0}"'.format(name)
    if not present:
        yield 'apt-add-repository -y --remove "{0}"'.format(name)