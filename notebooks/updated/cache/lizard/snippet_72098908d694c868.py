def perform_release(context):
    try:
        run_tests()
        if not context.skip_changelog:
            generate_changelog(context)
        increment_version(context)
        build_distributions(context)
        install_package(context)
        upload_package(context)
        install_from_pypi(context)
        publish(context)
    except Exception:
        log.exception('Error releasing')