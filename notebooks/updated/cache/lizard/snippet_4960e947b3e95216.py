def start_process(self, name):
    process_name, proc = self.new_process(name)
    LOGGER.info('Spawning %s process for %s', process_name, name)
    self.consumers[name].processes[process_name] = proc
    try:
        proc.start()
    except IOError as error:
        LOGGER.critical('Failed to start %s for %s: %r', process_name, name,
            error)
        del self.consumers[name].process[process_name]