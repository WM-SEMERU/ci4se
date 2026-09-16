def launch_cmd(self, n, force):
    check_permissions()
    prefix = self.conf.prefix
    maintag = self.conf.maintag
    commandStr = 'supervisord -c /etc/supervisor/conf.d/supervisord.conf'
    for i in range(1, n + 1):
        cName = '{0}-{1}'.format(prefix, i)
        if self.container_exists(name=cName):
            if not force:
                exit('Container with name {0} already exists.'.format(cName))
            else:
                if self.container_running(name=cName):
                    self.stop(cName)
                self.remove_container(cName, v=True)
        c = self.create_container(image=maintag, name=cName, command=
            commandStr, volumes=['/bricks'])
        self.start(c['Id'], privileged=True)
        time.sleep(2)
        echo('Launched {0} (Id: {1})'.format(cName, c['Id']))
        c = None
        cName = None