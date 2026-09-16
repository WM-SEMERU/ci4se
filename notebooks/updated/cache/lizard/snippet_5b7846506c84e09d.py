def mute(self):
    response = self.renderingControl.GetMute([('InstanceID', 0), ('Channel',
        'Master')])
    mute_state = response['CurrentMute']
    return bool(int(mute_state))