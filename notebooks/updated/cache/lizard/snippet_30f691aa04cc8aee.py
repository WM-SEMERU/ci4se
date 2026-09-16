def get_interpreter_path(version=None):
    if version and version != str(sys.version_info[0]):
        return settings.PYTHON_INTERPRETER + version
    else:
        return sys.executable