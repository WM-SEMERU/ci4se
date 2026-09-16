def removePage(self, pageId):
    try:
        self._pages[pageId].deleteLater()
        del self._pages[pageId]
    except KeyError:
        pass