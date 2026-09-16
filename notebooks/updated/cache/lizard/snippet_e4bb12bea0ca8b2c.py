def map_V_to_height(self, alat, alon, height, newheight, V):
    return self._map_EV_to_height(alat, alon, height, newheight, V, 'V')