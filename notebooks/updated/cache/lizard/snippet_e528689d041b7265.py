def wait_for_a_future(futures, print_traceback=False):
    while True:
        try:
            future = next(concurrent.futures.as_completed(futures, timeout=
                THREAD_TIMEOUT_MAX))
            break
        except concurrent.futures.TimeoutError:
            pass
        except KeyboardInterrupt:
            if print_traceback:
                traceback.print_stack()
            else:
                print('')
            os._exit(os.EX_IOERR)
    return future