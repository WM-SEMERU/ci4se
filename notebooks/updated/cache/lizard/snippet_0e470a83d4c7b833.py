async def _unsubscribe(self, channels, is_mask):
    vanished = []
    if channels:
        for channel in channels:
            key = channel, is_mask
            self._channels.remove(key)
            self._plugin._subscriptions[key].remove(self._queue)
            if not self._plugin._subscriptions[key]:
                vanished.append(channel)
                del self._plugin._subscriptions[key]
    else:
        while self._channels:
            channel, is_mask = key = self._channels.pop()
            self._plugin._subscriptions[key].remove(self._queue)
            if not self._plugin._subscriptions[key]:
                vanished.append(channel)
                del self._plugin._subscriptions[key]
    if vanished:
        await getattr(self._sub, 'punsubscribe' if is_mask else 'unsubscribe')(
            vanished)