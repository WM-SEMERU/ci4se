def playstate(state):
    if state is None:
        return const.PLAY_STATE_NO_MEDIA
    if state == 0:
        return const.PLAY_STATE_IDLE
    if state == 1:
        return const.PLAY_STATE_LOADING
    if state == 3:
        return const.PLAY_STATE_PAUSED
    if state == 4:
        return const.PLAY_STATE_PLAYING
    if state == 5:
        return const.PLAY_STATE_FAST_FORWARD
    if state == 6:
        return const.PLAY_STATE_FAST_BACKWARD
    raise exceptions.UnknownPlayState('Unknown playstate: ' + str(state))