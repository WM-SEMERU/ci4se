def _restore_volume(self, fade):
    self.device.mute = self.mute
    if self.volume == 100:
        fixed_vol = self.device.renderingControl.GetOutputFixed([(
            'InstanceID', 0)])['CurrentFixed']
    else:
        fixed_vol = False
    if not fixed_vol:
        self.device.bass = self.bass
        self.device.treble = self.treble
        self.device.loudness = self.loudness
        if fade:
            self.device.volume = 0
            self.device.ramp_to_volume(self.volume)
        else:
            self.device.volume = self.volume