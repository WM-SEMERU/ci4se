def set_position(self, key, latlon, layer=None, rotation=0):
    self.object_queue.put(SlipPosition(key, latlon, layer, rotation))