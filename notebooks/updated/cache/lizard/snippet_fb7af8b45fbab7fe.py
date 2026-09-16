def start(self):
    self.started = True
    if self.app:
        web_port = self.config['network']['web_port']
        logger.info('Starting server listening on port {0}'.format(web_port))
        key_file = os.path.join(self.work_dir, 'server.key')
        cert_file = os.path.join(self.work_dir, 'server.crt')
        http_server = WSGIServer(('', web_port), self.app, keyfile=key_file,
            certfile=cert_file)
        http_server_greenlet = gevent.spawn(http_server.serve_forever)
        self.greenlets.append(http_server_greenlet)
    stop_if_not_write_workdir(self.work_dir)
    logger.info('Server started.')
    gevent.joinall(self.greenlets)