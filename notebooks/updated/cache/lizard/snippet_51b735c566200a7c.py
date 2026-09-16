def get_resource_path(venv, package=None, resource=None):
    _verify_safe_py_code(package, resource)
    bin_path = _verify_virtualenv(venv)
    ret = __salt__['cmd.exec_code_all'](bin_path,
        "import pkg_resources; print(pkg_resources.resource_filename('{0}', '{1}'))"
        .format(package, resource))
    if ret['retcode'] != 0:
        raise CommandExecutionError('{stdout}\n{stderr}'.format(**ret))
    return ret['stdout']