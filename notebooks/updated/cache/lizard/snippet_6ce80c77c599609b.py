def set_display_mode(self, zoom, layout='continuous'):
    if (zoom == 'fullpage' or zoom == 'fullwidth' or zoom == 'real' or zoom ==
        'default' or not isinstance(zoom, basestring)):
        self.zoom_mode = zoom
    else:
        self.error('Incorrect zoom display mode: ' + zoom)
    if (layout == 'single' or layout == 'continuous' or layout == 'two' or 
        layout == 'default'):
        self.layout_mode = layout
    else:
        self.error('Incorrect layout display mode: ' + layout)