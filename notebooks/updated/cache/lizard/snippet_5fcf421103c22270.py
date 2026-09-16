def _fix_syscall_ip(state):
    try:
        bypass = o.BYPASS_UNSUPPORTED_SYSCALL in state.options
        stub = state.project.simos.syscall(state, allow_unsupported=bypass)
        if stub:
            state.ip = stub.addr
    except AngrUnsupportedSyscallError:
        pass