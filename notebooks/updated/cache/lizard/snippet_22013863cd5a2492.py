def launch_thread(self, name, fn, *args, **kwargs):
    logger.debug("Launching thread '%s': %s(%s, %s)", name, fn, args, kwargs)
    self.thread_pool[name] = threading.Thread(target=fn, args=args, kwargs=
        kwargs)
    self.thread_pool[name].daemon = True
    self.thread_pool[name].start()