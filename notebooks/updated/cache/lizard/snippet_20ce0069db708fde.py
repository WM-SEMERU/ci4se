def submit(self, data, runtime_dir, argv):
    logger.debug(__("Connector '{}' running for Data with id {} ({}).",
        self.__class__.__module__, data.id, repr(argv)))
    subprocess.Popen(argv, cwd=runtime_dir, stdin=subprocess.DEVNULL).wait()