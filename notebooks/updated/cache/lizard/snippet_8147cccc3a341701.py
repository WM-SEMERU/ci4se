def get_current_thread_id(thread):
    try:
        tid = thread.__pydevd_id__
        if tid is None:
            raise AttributeError()
    except AttributeError:
        tid = _get_or_compute_thread_id_with_lock(thread, is_current_thread
            =True)
    return tid