def _import_packages(packages, optional=None):
    if not optional:
        optional = []
    package_references = set()
    failures = set()
    for package_name in packages:
        try:
            package_reference = __import__(package_name, globals(), locals(
                ), [], 0)
            package_references.add(package_reference)
        except ImportError:
            failures.add(package_name)
    if failures:
        raise ImportError('Unable to find required packages: {0}'.format(
            ', '.join(failures)))
    failures = set()
    for package_name in optional:
        try:
            package_reference = __import__(package_name, globals(), locals(
                ), [], 0)
            package_references.add(package_reference)
        except ImportError:
            failures.add(package_name)
    for failure in failures:
        warn(ImportWarning('Unable to import {0}'.format(failure)))
    return package_references