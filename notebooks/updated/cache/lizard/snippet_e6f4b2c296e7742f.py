def pkg_supports(feature, pkg_version, pkg_feat_dict):
    from pkg_resources import parse_requirements
    feature = str(feature)
    pkg_version = str(pkg_version)
    supp_versions = pkg_feat_dict.get(feature, None)
    if supp_versions is None:
        return False
    if is_string(supp_versions):
        supp_versions = [supp_versions]
    ver_specs = [('pkg' + supp_ver) for supp_ver in supp_versions]
    ver_reqs = [list(parse_requirements(ver_spec))[0] for ver_spec in ver_specs
        ]
    for req in ver_reqs:
        if req.specifier.contains(pkg_version, prereleases=True):
            return True
    return False