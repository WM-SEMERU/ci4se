def prev_img_ws(self, ws, loop=True):
    channel = self.get_active_channel_ws(ws)
    if channel is None:
        return
    channel.prev_image()
    return True