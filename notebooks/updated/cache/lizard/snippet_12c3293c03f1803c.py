def get_version(form='short'):
    versions = {}
    branch = '%s.%s' % (VERSION[0], VERSION[1])
    tertiary = VERSION[2]
    type_ = VERSION[3]
    type_num = VERSION[4]
    versions['branch'] = branch
    v = versions['branch']
    if tertiary:
        versions['tertiary'] = '.' + str(tertiary)
        v += versions['tertiary']
    versions['short'] = v
    if form is 'short':
        return v
    v += ' ' + type_ + ' ' + str(type_num)
    versions['normal'] = v
    if form is 'normal':
        return v
    v += ' @' + git_sha()
    versions['verbose'] = v
    if form is 'verbose':
        return v
    if form is 'all':
        return versions