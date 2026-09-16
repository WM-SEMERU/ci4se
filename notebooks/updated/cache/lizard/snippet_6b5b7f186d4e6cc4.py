def start(self):
    fname = self.conf['file']
    logging.info(
        "Configfile watcher plugin: Starting to watch route spec file '%s' for changes..."
         % fname)
    route_spec = {}
    try:
        route_spec = read_route_spec_config(fname)
        if route_spec:
            self.last_route_spec_update = datetime.datetime.now()
            self.q_route_spec.put(route_spec)
    except ValueError as e:
        logging.warning('Cannot parse route spec: %s' % str(e))
    abspath = os.path.abspath(fname)
    parent_dir = os.path.dirname(abspath)
    handler = RouteSpecChangeEventHandler(route_spec_fname=fname,
        route_spec_abspath=abspath, q_route_spec=self.q_route_spec, plugin=self
        )
    self.observer_thread = watchdog.observers.Observer()
    self.observer_thread.name = 'ConfMon'
    self.observer_thread.schedule(handler, parent_dir)
    self.observer_thread.start()