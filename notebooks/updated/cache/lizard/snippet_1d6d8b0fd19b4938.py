def play_empty(self):
    if self.vclient:
        if self.streamer:
            self.streamer.volume = 0
        self.vclient.play_audio('\n'.encode(), encode=False)