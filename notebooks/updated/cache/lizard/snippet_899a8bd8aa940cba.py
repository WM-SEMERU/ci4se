def _needs_hiding(mod_name):
    pattern = re.compile('(setuptools|pkg_resources|distutils|Cython)(\\.|$)')
    return bool(pattern.match(mod_name))