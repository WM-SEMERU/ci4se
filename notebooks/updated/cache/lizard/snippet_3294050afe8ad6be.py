def on(self):
    assert spotifyconnect._session_instance.player.num_listeners(spotifyconnect
        .PlayerEvent.MUSIC_DELIVERY) == 0
    spotifyconnect._session_instance.player.on(spotifyconnect.PlayerEvent.
        MUSIC_DELIVERY, self._on_music_delivery)