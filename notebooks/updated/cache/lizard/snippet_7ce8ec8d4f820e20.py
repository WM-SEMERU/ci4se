def kill_child_processes(parent_proc):
    logging.debug('Killing stress process')
    try:
        for proc in parent_proc.children(recursive=True):
            logging.debug('Killing %s', proc)
            proc.kill()
        parent_proc.kill()
    except AttributeError:
        logging.debug('No such process')
        logging.debug('Could not kill process')