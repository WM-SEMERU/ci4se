def render_js_code(self, id_, *args, **kwargs):
    if id_:
        options = self.render_select2_options_code(dict(self.get_options()),
            id_)
        return mark_safe(self.html.format(id=id_, options=options))
    return ''