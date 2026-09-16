def manage(self):
    hookenv._run_atstart()
    try:
        hook_name = hookenv.hook_name()
        if hook_name == 'stop':
            self.stop_services()
        else:
            self.reconfigure_services()
            self.provide_data()
    except SystemExit as x:
        if x.code is None or x.code == 0:
            hookenv._run_atexit()
    hookenv._run_atexit()