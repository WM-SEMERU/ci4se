def on_audio_adapter_change(self, audio_adapter):
    if not isinstance(audio_adapter, IAudioAdapter):
        raise TypeError(
            'audio_adapter can only be an instance of type IAudioAdapter')
    self._call('onAudioAdapterChange', in_p=[audio_adapter])