def _highlight_path(self, hl_path, tf):
    fc = self.settings.get('row_font_color', 'green')
    try:
        self.treeview.highlight_path(hl_path, tf, font_color=fc)
    except Exception as e:
        self.logger.info('Error changing highlight on treeview path ({0}): {1}'
            .format(hl_path, str(e)))