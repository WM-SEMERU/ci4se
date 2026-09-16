def set_effect(self, effect_name: str):
    try:
        effect_index = self._light_effect_list.index(effect_name)
    except ValueError:
        LOG.error('Trying to set unknown light effect')
        return False
    return self.setValue(key='PROGRAM', channel=self._effect_channel, value
        =effect_index)