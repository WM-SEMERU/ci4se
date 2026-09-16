def __get_supervisor(self):
    options = supervisorctl.ClientOptions()
    options.realize(args=['-c', self.supervisord_conf_path])
    return supervisorctl.Controller(options).get_supervisor()