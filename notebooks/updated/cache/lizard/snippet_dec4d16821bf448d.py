def run_coroutine(self, cor, *args, **kwargs):
    if self.stopping:
        raise LoopStoppingError(
            'Could not launch coroutine because loop is shutting down: %s' %
            cor)
    self.start()
    cor = _instaniate_coroutine(cor, args, kwargs)
    if self.inside_loop():
        raise InternalError(
            'BackgroundEventLoop.run_coroutine called from inside event loop, would have deadlocked.'
            )
    future = self.launch_coroutine(cor)
    return future.result()