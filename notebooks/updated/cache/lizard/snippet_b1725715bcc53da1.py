def parse_pkg_ver(self, want_installed):
    all_versions = []
    arg_str = ''.join(self.pkg_spec)
    if '==' not in arg_str:
        project_name = arg_str
        version = None
    else:
        project_name, version = arg_str.split('==')
        project_name = project_name.strip()
        version = version.strip()
    if want_installed:
        dists = Distributions()
        project_name = dists.case_sensitive_name(project_name)
    else:
        project_name, all_versions = self.pypi.query_versions_pypi(project_name
            )
        if not len(all_versions):
            msg = "I'm afraid we have no '%s' at " % project_name
            msg += 'The Cheese Shop. A little Red Leicester, perhaps?'
            self.logger.error(msg)
            sys.exit(2)
    return project_name, version, all_versions