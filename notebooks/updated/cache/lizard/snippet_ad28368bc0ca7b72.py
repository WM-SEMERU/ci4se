def check_deps(deps):
    if not isinstance(deps, list):
        deps = [deps]
    checks = list(Environment.has_apps(deps))
    if not all(checks):
        for name, available in list(dict(zip(deps, checks)).items()):
            if not available:
                error_msg = (
                    "The required application/dependency '{0}' isn't available."
                    .format(name))
                raise SystemError(error_msg)