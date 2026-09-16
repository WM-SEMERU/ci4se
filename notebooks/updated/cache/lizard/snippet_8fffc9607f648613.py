def _on_fork(cls):
    cls._cls_idle_socketpairs = []
    while cls._cls_all_sockets:
        cls._cls_all_sockets.pop().close()