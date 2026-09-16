def go_to_preset(self, action=None, channel=0, preset_point_number=1):
    ret = self.command(
        'ptz.cgi?action={0}&channel={1}&code=GotoPreset&arg1=0&arg2={2}&arg3=0'
        .format(action, channel, preset_point_number))
    return ret.content.decode('utf-8')