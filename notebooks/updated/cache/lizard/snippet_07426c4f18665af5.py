def start(cls, _init_logging=True):
    if cls.worker_sock is not None:
        return
    if faulthandler is not None:
        faulthandler.enable()
    mitogen.utils.setup_gil()
    cls.unix_listener_path = mitogen.unix.make_socket_path()
    cls.worker_sock, cls.child_sock = socket.socketpair()
    atexit.register(lambda : clean_shutdown(cls.worker_sock))
    mitogen.core.set_cloexec(cls.worker_sock.fileno())
    mitogen.core.set_cloexec(cls.child_sock.fileno())
    cls.profiling = os.environ.get('MITOGEN_PROFILING') is not None
    if cls.profiling:
        mitogen.core.enable_profiling()
    if _init_logging:
        ansible_mitogen.logging.setup()
    cls.original_env = dict(os.environ)
    cls.child_pid = os.fork()
    if cls.child_pid:
        save_pid('controller')
        ansible_mitogen.logging.set_process_name('top')
        ansible_mitogen.affinity.policy.assign_controller()
        cls.child_sock.close()
        cls.child_sock = None
        mitogen.core.io_op(cls.worker_sock.recv, 1)
    else:
        save_pid('mux')
        ansible_mitogen.logging.set_process_name('mux')
        ansible_mitogen.affinity.policy.assign_muxprocess()
        cls.worker_sock.close()
        cls.worker_sock = None
        self = cls()
        self.worker_main()