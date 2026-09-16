def play_mode(self, playmode):
    playmode = playmode.upper()
    if playmode not in PLAY_MODES.keys():
        raise KeyError("'%s' is not a valid play mode" % playmode)
    self.avTransport.SetPlayMode([('InstanceID', 0), ('NewPlayMode', playmode)]
        )