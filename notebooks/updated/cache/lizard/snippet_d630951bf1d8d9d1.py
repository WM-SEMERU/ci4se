def tty_create_child(args):
    master_fd, slave_fd = openpty()
    try:
        mitogen.core.set_block(slave_fd)
        disable_echo(master_fd)
        disable_echo(slave_fd)
        pid = detach_popen(args=args, stdin=slave_fd, stdout=slave_fd,
            stderr=slave_fd, preexec_fn=_acquire_controlling_tty, close_fds
            =True)
    except Exception:
        os.close(master_fd)
        os.close(slave_fd)
        raise
    os.close(slave_fd)
    LOG.debug('tty_create_child() child %d fd %d, parent %d, cmd: %s', pid,
        master_fd, os.getpid(), Argv(args))
    return pid, master_fd, None