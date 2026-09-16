def get_delete_url_link(self, text=None, cls=None, icon_class=None, **attrs):
    if text is None:
        text = 'Delete'
    return build_link(href=self.get_delete_url(), text=text, cls=cls,
        icon_class=icon_class, **attrs)