def send_scp(self, *args, **kwargs):
    cabinet = kwargs.pop('cabinet')
    frame = kwargs.pop('frame')
    board = kwargs.pop('board')
    return self._send_scp(cabinet, frame, board, *args, **kwargs)