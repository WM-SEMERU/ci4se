def run_app(self):
    sys.argv[0] = sys.executable
    sys.argv[1] = '{}.py'.format(sys.argv[1])
    self._app_process = subprocess.Popen(sys.argv)
    return self._app_process.wait()