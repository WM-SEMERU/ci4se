def render_urchin(self, ctx, data):
    key = APIKey.getKeyForAPI(self._siteStore(), APIKey.URCHIN)
    if key is None:
        return ''
    return ctx.tag.fillSlots('urchin-key', key.apiKey)