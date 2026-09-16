def check_streamers(self, blacklist=None):
    ready = []
    selected = set()
    for i, streamer in enumerate(self.streamers):
        if blacklist is not None and i in blacklist:
            continue
        if i in selected:
            continue
        marked = False
        if i in self._manually_triggered_streamers:
            marked = True
            self._manually_triggered_streamers.remove(i)
        if streamer.triggered(marked):
            self._logger.debug('Streamer %d triggered, manual=%s', i, marked)
            ready.append(streamer)
            selected.add(i)
            for j, streamer2 in enumerate(self.streamers[i:]):
                if (streamer2.with_other == i and j not in selected and
                    streamer2.triggered(True)):
                    self._logger.debug(
                        'Streamer %d triggered due to with-other on %d', j, i)
                    ready.append(streamer2)
                    selected.add(j)
    return ready