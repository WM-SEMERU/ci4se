def interrupt_stdin_thread():
    dupped_stdin = os.dup(0)
    assert not the_stdin_thread.interrupt_asked
    the_stdin_thread.interrupt_asked = True
    os.lseek(tempfile_fd, 0, 0)
    os.dup2(tempfile_fd, 0)
    pid = get_stdin_pid()
    os.kill(pid, signal.SIGWINCH)
    the_stdin_thread.out_of_raw_input.wait()
    the_stdin_thread.interrupt_asked = False
    os.dup2(dupped_stdin, 0)
    os.close(dupped_stdin)