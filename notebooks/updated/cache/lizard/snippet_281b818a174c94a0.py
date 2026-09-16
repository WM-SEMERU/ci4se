def gc_stop():
    global gc_thread
    if gc_thread:
        log.info('Shutting down GC thread')
        gc_thread.signal_stop()
        gc_thread.join()
        log.info('GC thread joined')
        gc_thread = None
    else:
        log.info('GC thread already joined')