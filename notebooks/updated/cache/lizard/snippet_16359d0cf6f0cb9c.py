def _getVirtualScreenBitmap(self):
    min_x, min_y, screen_width, screen_height = self._getVirtualScreenRect()
    monitors = self._getMonitorInfo()
    virt_screen = Image.new('RGB', (screen_width, screen_height))
    for monitor_id in range(0, len(monitors)):
        img = self._captureScreen(monitors[monitor_id]['name'])
        x1, y1, x2, y2 = monitors[monitor_id]['rect']
        x = x1 - min_x
        y = y1 - min_y
        virt_screen.paste(img, (x, y))
    return virt_screen