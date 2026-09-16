def update(self, friendly_name, enabled=values.unset, video_layout=values.
    unset, audio_sources=values.unset, audio_sources_excluded=values.unset,
    trim=values.unset, format=values.unset, resolution=values.unset,
    status_callback=values.unset, status_callback_method=values.unset):
    return self._proxy.update(friendly_name, enabled=enabled, video_layout=
        video_layout, audio_sources=audio_sources, audio_sources_excluded=
        audio_sources_excluded, trim=trim, format=format, resolution=
        resolution, status_callback=status_callback, status_callback_method
        =status_callback_method)