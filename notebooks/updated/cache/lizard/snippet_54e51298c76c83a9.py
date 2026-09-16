def rpm_versioned_name(cls, name, version, default_number=False):
    regexp = re.compile('^python(\\d*|)-(.*)')
    auto_provides_regexp = re.compile('^python(\\d*|)dist(.*)')
    if not version or version == cls.get_default_py_version(
        ) and not default_number:
        found = regexp.search(name)
        if found and found.group(2) != 'devel':
            if 'epel' not in cls.template:
                return 'python-{0}'.format(regexp.search(name).group(2))
        return name
    versioned_name = name
    if version:
        if regexp.search(name):
            versioned_name = re.sub('^python(\\d*|)-', 'python{0}-'.format(
                version), name)
        elif auto_provides_regexp.search(name):
            versioned_name = re.sub('^python(\\d*|)dist', 'python{0}dist'.
                format(version), name)
        else:
            versioned_name = 'python{0}-{1}'.format(version, name)
        if 'epel' in cls.template and version != cls.get_default_py_version():
            versioned_name = versioned_name.replace('{0}'.format(version),
                '%{{python{0}_pkgversion}}'.format(version))
    return versioned_name