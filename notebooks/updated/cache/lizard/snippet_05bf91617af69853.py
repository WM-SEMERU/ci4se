def zoom_in(self):
    viewer = self.getfocus_viewer()
    if hasattr(viewer, 'zoom_in'):
        viewer.zoom_in()
    return True