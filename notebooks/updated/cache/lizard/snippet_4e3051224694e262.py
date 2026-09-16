def cmd_imap(self, nm=None, ch=None):
    viewer = self.get_viewer(ch)
    if viewer is None:
        self.log('No current viewer/channel.')
        return
    if nm is None:
        rgbmap = viewer.get_rgbmap()
        imap = rgbmap.get_imap()
        self.log(imap.name)
    else:
        viewer.set_intensity_map(nm)