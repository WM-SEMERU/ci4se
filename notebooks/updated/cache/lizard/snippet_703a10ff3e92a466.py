def zoom_cb(self, fitsimage, event):
    chviewer = self.fv.getfocus_viewer()
    bd = chviewer.get_bindings()
    if hasattr(bd, 'sc_zoom'):
        return bd.sc_zoom(chviewer, event)
    return False