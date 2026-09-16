def _pipe_stdio(cls, sock, stdin_isatty, stdout_isatty, stderr_isatty,
    handle_stdin):
    stdio_writers = (ChunkType.STDOUT, stdout_isatty), (ChunkType.STDERR,
        stderr_isatty)
    types, ttys = zip(*stdio_writers)

    @contextmanager
    def maybe_handle_stdin(want):
        if want:
            with NailgunStreamStdinReader.open(sock, stdin_isatty) as fd:
                yield fd
        else:
            with open('/dev/null', 'rb') as fh:
                yield fh.fileno()
    with maybe_handle_stdin(handle_stdin
        ) as stdin_fd, NailgunStreamWriter.open_multi(sock, types, ttys) as ((
        stdout_fd, stderr_fd), writer), stdio_as(stdout_fd=stdout_fd,
        stderr_fd=stderr_fd, stdin_fd=stdin_fd):
        stdout, stderr = sys.stdout, sys.stderr

        def finalizer():
            try:
                stdout.flush()
                stderr.flush()
            finally:
                time.sleep(0.001)
                writer.stop()
                writer.join()
                stdout.close()
                stderr.close()
        yield finalizer