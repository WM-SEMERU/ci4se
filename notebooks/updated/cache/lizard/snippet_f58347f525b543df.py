def _WaitForStartup(self, deadline):
    start = time.time()
    sleep = 0.05

    def Elapsed():
        return time.time() - start
    while True:
        try:
            response, _ = self._http.request(self._host)
            if response.status == 200:
                logging.info('emulator responded after %f seconds', Elapsed())
                return True
        except (socket.error, httplib.ResponseNotReady):
            pass
        if Elapsed() >= deadline:
            return False
        else:
            time.sleep(sleep)
            sleep *= 2