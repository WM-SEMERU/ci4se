def using_bzr(cwd):
    try:
        bzr_log = shell_out(['bzr', 'log'], cwd=cwd)
        return True
    except (CalledProcessError, OSError):
        return False