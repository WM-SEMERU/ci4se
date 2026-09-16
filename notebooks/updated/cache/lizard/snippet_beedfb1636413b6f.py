def uninstall_package(package_name, service_name=None, all_instances=False,
    wait_for_completion=False, timeout_sec=600):
    package_manager = _get_package_manager()
    pkg = package_manager.get_package_version(package_name, None)
    try:
        if service_name is None:
            service_name = _get_service_name(package_name, pkg)
        print("{}uninstalling package '{}' with service name '{}'\n".format
            (shakedown.cli.helpers.fchr('>>'), package_name, service_name))
        package_manager.uninstall_app(package_name, all_instances, service_name
            )
        if wait_for_completion:
            wait_for_mesos_task_removal(service_name, timeout_sec=timeout_sec)
    except errors.DCOSException as e:
        print('\n{}{}'.format(shakedown.cli.helpers.fchr('>>'), e))
    if pkg.cli_definition():
        print("{}uninstalling CLI commands for package '{}'".format(
            shakedown.cli.helpers.fchr('>>'), package_name))
        subcommand.uninstall(package_name)
    return True