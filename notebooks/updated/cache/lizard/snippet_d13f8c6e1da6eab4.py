def web_preview(self):
    if isinstance(self.media, types.MessageMediaWebPage):
        if isinstance(self.media.webpage, types.WebPage):
            return self.media.webpage