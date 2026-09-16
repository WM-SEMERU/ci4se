def executable_path(conn, executable):
    executable_path = conn.remote_module.which(executable)
    if not executable_path:
        raise ExecutableNotFound(executable, conn.hostname)
    return executable_path