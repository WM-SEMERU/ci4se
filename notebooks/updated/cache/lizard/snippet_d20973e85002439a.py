def ttynames_from_env(cls, env):
    return tuple(env.get(cls.TTY_PATH_ENV.format(fd_id)) for fd_id in
        STDIO_DESCRIPTORS)