def exact_or_minor_exe_version_match(executable_name, exe_version_tuples,
    version):
    exe = exact_exe_version_match(executable_name, exe_version_tuples, version)
    if not exe:
        exe = minor_exe_version_match(executable_name, exe_version_tuples,
            version)
    return exe