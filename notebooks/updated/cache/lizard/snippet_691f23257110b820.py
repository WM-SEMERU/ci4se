async def handle_event(self, event: 'node.LavalinkEvents', extra):
    if event == LavalinkEvents.TRACK_END:
        if extra == TrackEndReason.FINISHED:
            await self.play()
        else:
            self._is_playing = False