def play(self, sox_effects=()):
    preloader_threads = []
    if self.text != '-':
        segments = list(self)
        preloader_threads = [PreloaderThread(name='PreloaderThread-%u' % i) for
            i in range(PRELOADER_THREAD_COUNT)]
        for preloader_thread in preloader_threads:
            preloader_thread.segments = segments
            preloader_thread.start()
    else:
        segments = iter(self)
    for segment in segments:
        segment.play(sox_effects)
    if self.text != '-':
        for preloader_thread in preloader_threads:
            preloader_thread.join()