def stop(self):
    try:
        self.shutdown()
    except (PyMongoError, ServersError) as exc:
        logger.info('Killing %s with signal, shutdown command failed: %r',
            self.name, exc)
        return process.kill_mprocess(self.proc)