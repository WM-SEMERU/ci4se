def acceptNavigationRequest(self, url, kind, is_main_frame):
    ready_url = url.toEncoded().data().decode()
    is_clicked = kind == self.NavigationTypeLinkClicked
    if is_clicked and self.root_url not in ready_url:
        QtGui.QDesktopServices.openUrl(url)
        return False
    return super(WebPage, self).acceptNavigationRequest(url, kind,
        is_main_frame)