def make_std_api(python_version=sys.version_info, variant=VARIANT):
    if isinstance(python_version, float):
        major = int(python_version)
        minor = int((python_version - major + 0.05) * 10)
        python_version = major, minor
    return _StdApi(python_version, variant)