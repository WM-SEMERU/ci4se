def _get_ui_content(self, cli, width, height):

    def get_content():
        return self.content.create_content(cli, width=width, height=height)
    key = cli.render_counter, width, height
    return self._ui_content_cache.get(key, get_content)