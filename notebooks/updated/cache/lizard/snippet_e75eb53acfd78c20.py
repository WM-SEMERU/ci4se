def create_open(cls, *args, **kwargs):

    def f(seed_tuple):
        j = cls(seed_tuple, *args, **kwargs)

        def wait_loop():
            bot, msg, seed = seed_tuple
            try:
                handled = j.open(msg, seed)
                if not handled:
                    j.on_message(msg)
                while 1:
                    msg = j.listener.wait()
                    j.on_message(msg)
            except (exception.IdleTerminate, exception.StopListening) as e:
                j.on_close(e)
            except Exception as e:
                traceback.print_exc()
                j.on_close(e)
        return wait_loop
    return f