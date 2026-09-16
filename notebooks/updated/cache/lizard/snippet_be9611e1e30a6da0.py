def build_deps(self):
    build_requires = self.metadata['setup_requires']
    if self.has_test_suite:
        build_requires += self.metadata['tests_require'] + self.metadata[
            'install_requires']
    if 'setuptools' not in build_requires:
        build_requires.append('setuptools')
    return sorted(self.name_convert_deps_list(deps_from_pyp_format(
        build_requires, runtime=False)))