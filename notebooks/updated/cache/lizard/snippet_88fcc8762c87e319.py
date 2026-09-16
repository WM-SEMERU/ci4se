def start(self, log_file='/tmp/hgserver.log', log_level=logging.INFO):
    for puid in list(self.processes.keys()):
        print('terminating:', puid)
        self.processes[puid].terminate()
        del self.processes[puid]
    self.app = create_app(self.tilesets, __name__, log_file=log_file,
        log_level=log_level, file_ids=self.file_ids)
    uuid = slugid.nice()
    if self.port is None:
        self.port = get_open_port()
    target = partial(self.app.run, threaded=True, debug=True, host=
        '0.0.0.0', port=self.port, use_reloader=False)
    self.processes[uuid] = mp.Process(target=target)
    self.processes[uuid].start()
    self.connected = False
    while not self.connected:
        try:
            url = 'http://{}:{}/api/v1'.format(self.host, self.port)
            r = requests.head(url)
            if r.ok:
                self.connected = True
        except requests.ConnectionError as err:
            time.sleep(0.2)