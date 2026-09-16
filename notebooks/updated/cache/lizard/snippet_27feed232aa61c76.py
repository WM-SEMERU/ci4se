def update(self, language=values.unset, tagged_text=values.unset,
    source_channel=values.unset):
    return self._proxy.update(language=language, tagged_text=tagged_text,
        source_channel=source_channel)