def render_to_console(self, message: str, **kwargs):
    rendered = templating.render(message, **kwargs)
    return self.write_to_console(rendered)