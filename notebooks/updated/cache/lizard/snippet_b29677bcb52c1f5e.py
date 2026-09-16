def schedCoro(self, coro):
    import synapse.lib.provenance as s_provenance
    if __debug__:
        assert s_coro.iscoro(coro)
        import synapse.lib.threads as s_threads
        assert s_threads.iden() == self.tid
    task = self.loop.create_task(coro)
    if asyncio.current_task():
        s_provenance.dupstack(task)

    def taskDone(task):
        self._active_tasks.remove(task)
        try:
            task.result()
        except asyncio.CancelledError:
            pass
        except Exception:
            logger.exception(
                'Task scheduled through Base.schedCoro raised exception')
    self._active_tasks.add(task)
    task.add_done_callback(taskDone)
    return task