def autoconnect():
    if not USE_AUTOCONNECT:
        return
    try:
        import pyudev
    except ImportError:
        return
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    connect_thread = threading.Thread(target=autoconnect_thread, args=(
        monitor,), name='AutoConnect')
    connect_thread.daemon = True
    connect_thread.start()