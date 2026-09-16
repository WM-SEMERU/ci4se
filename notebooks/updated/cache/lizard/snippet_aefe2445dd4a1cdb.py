def main(self):
    try:
        if not self.verify_only and not self.do_daemon_init_and_start():
            self.exit_on_error(message='Daemon initialization error',
                exit_code=3)
        if self.verify_only:
            self.setup_alignak_logger()
        self.load_monitoring_config_file()
        self.set_proctitle(self.name)
        self.modules_manager.start_external_instances()
        self.hook_point('load_retention')
        while True:
            self.do_main_loop()
            logger.info('Exited from the main loop.')
            if not self.need_config_reload:
                self.request_stop()
            else:
                while self.need_config_reload:
                    self.need_config_reload = False
                    self.link_to_myself = None
                    self.conf = Config()
                    _ts = time.time()
                    logger.warning('--- Reloading configuration...')
                    self.load_monitoring_config_file()
                    duration = int(time.time() - _ts)
                    self.add(make_monitoring_log('info', 
                        'CONFIGURATION RELOAD;%d' % duration))
                    logger.warning('--- Configuration reloaded, %d seconds',
                        duration)
                    pause = max(1, self.conf.daemons_new_conf_timeout)
                    if pause:
                        logger.info('Pausing %.2f seconds...', pause)
                        time.sleep(pause)
    except Exception as exp:
        if self.is_master:
            self.daemons_stop(timeout=self.conf.daemons_stop_timeout)
        self.exit_on_exception(raised_exception=exp)
        raise