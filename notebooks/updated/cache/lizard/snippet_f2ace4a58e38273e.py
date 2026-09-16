def set_rich_menu_image(self, rich_menu_id, content_type, content, timeout=None
    ):
    self._post('/v2/bot/richmenu/{rich_menu_id}/content'.format(
        rich_menu_id=rich_menu_id), data=content, headers={'Content-Type':
        content_type}, timeout=timeout)