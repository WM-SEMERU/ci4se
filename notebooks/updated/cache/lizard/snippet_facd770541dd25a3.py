def progress_string(self):
    if not self.last_result:
        return self._status_string()

    def location_string(hostname, pid):
        if hostname == os.uname()[1]:
            return 'pid={}'.format(pid)
        else:
            return '{} pid={}'.format(hostname, pid)
    pieces = ['{}'.format(self._status_string()), '[{}]'.format(self.
        resources.summary_string()), '[{}]'.format(location_string(self.
        last_result.get(HOSTNAME), self.last_result.get(PID))), '{} s'.
        format(int(self.last_result.get(TIME_TOTAL_S)))]
    if self.last_result.get(TRAINING_ITERATION) is not None:
        pieces.append('{} iter'.format(self.last_result[TRAINING_ITERATION]))
    if self.last_result.get(TIMESTEPS_TOTAL) is not None:
        pieces.append('{} ts'.format(self.last_result[TIMESTEPS_TOTAL]))
    if self.last_result.get(EPISODE_REWARD_MEAN) is not None:
        pieces.append('{} rew'.format(format(self.last_result[
            EPISODE_REWARD_MEAN], '.3g')))
    if self.last_result.get(MEAN_LOSS) is not None:
        pieces.append('{} loss'.format(format(self.last_result[MEAN_LOSS],
            '.3g')))
    if self.last_result.get(MEAN_ACCURACY) is not None:
        pieces.append('{} acc'.format(format(self.last_result[MEAN_ACCURACY
            ], '.3g')))
    return ', '.join(pieces)