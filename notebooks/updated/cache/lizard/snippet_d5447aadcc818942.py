def pt_fingerprint(query):
    if not have_program('pt-fingerprint'):
        raise OSError("pt-fingerprint doesn't appear to be installed")
    thread = PTFingerprintThread.get_thread()
    thread.in_queue.put(query)
    return thread.out_queue.get()