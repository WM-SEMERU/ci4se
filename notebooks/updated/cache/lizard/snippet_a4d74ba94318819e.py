def check_pypi_updates(dependencies):
    dependencies_up_to_date = []
    for dependency in dependencies.get('pypi', []):
        try:
            latest_version = get_latest_version_number(dependency.project_name)
        except Exception as error:
            logger.warning('--check-updates command will be aborted. Error: %s'
                , error)
            return dependencies
        required_version = None
        if dependency.specs:
            _, required_version = dependency.specs[0]
        if required_version:
            dependencies_up_to_date.append(dependency)
            if latest_version > required_version:
                logger.info('There is a new version of %s: %s', dependency.
                    project_name, latest_version)
            elif latest_version < required_version:
                logger.warning(
                    'The requested version for %s is greater than latest found in PyPI: %s'
                    , dependency.project_name, latest_version)
            else:
                logger.info(
                    'The requested version for %s is the latest one in PyPI: %s'
                    , dependency.project_name, latest_version)
        else:
            project_name_plus = '{}=={}'.format(dependency.project_name,
                latest_version)
            dependencies_up_to_date.append(pkg_resources.Requirement.parse(
                project_name_plus))
            logger.info('The latest version of %r is %s and will use it.',
                dependency.project_name, latest_version)
    dependencies['pypi'] = dependencies_up_to_date
    return dependencies