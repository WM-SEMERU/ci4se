def freeze():
    echo_waiting('Verifying collected packages...')
    catalog, errors = make_catalog()
    if errors:
        for error in errors:
            echo_failure(error)
        abort()
    static_file = get_agent_requirements()
    echo_info('Static file: {}'.format(static_file))
    pre_packages = list(read_packages(static_file))
    catalog.write_packages(static_file)
    post_packages = list(read_packages(static_file))
    display_package_changes(pre_packages, post_packages)