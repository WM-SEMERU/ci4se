def send_audio(self, left_channel, right_channel, frame_counter=None):
    if frame_counter is None:
        frame_counter = self.audio_frame_counter
        self.audio_frame_counter += 1
    self.q_audio.put((frame_counter, left_channel, right_channel))