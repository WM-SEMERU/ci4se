def remove_sonos_playlist(self, sonos_playlist):
    object_id = getattr(sonos_playlist, 'item_id', sonos_playlist)
    return self.contentDirectory.DestroyObject([('ObjectID', object_id)])