def run_queue(self, options, todo):
    utils.logging_debug('AutoBatcher(%s): %d items', self._todo_tasklet.
        __name__, len(todo))
    batch_fut = self._todo_tasklet(todo, options)
    self._running.append(batch_fut)
    batch_fut.add_callback(self._finished_callback, batch_fut, todo)