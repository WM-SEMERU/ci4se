def createPlaylist(self, title, items=None, section=None, limit=None, smart
    =None, **kwargs):
    return Playlist.create(self, title, items=items, limit=limit, section=
        section, smart=smart, **kwargs)