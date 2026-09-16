def _ProcessAudio(self, tag, wall_time, step, audio):
    event = AudioEvent(wall_time=wall_time, step=step, encoded_audio_string
        =audio.encoded_audio_string, content_type=audio.content_type,
        sample_rate=audio.sample_rate, length_frames=audio.length_frames)
    self.audios.AddItem(tag, event)