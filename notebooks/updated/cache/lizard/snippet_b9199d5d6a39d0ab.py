def get_threadline_theming(self, thread):
    colours = int(self._config.get('colourmode'))
    return self._theme.get_threadline_theming(thread, colours)