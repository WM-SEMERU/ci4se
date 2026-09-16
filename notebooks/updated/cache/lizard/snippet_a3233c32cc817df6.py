def resume(self):
    if self.get_thread_count() == 0:
        self.scan_threads()
    resumed = list()
    try:
        for aThread in self.iter_threads():
            aThread.resume()
            resumed.append(aThread)
    except Exception:
        for aThread in resumed:
            try:
                aThread.suspend()
            except Exception:
                pass
        raise