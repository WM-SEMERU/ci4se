def render(self, form=None, **kwargs):
    context = self.get_context(**kwargs)
    return self.render_to_response(context)