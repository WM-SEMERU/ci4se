def makesvg(self, right_text, status=None, left_text=None, left_color=None,
    config=None):
    right_color = config['color_scheme'].get(status, '#9f9f9f')
    left_text = left_text or config['left_text']
    left_color = left_color or config['left_color']
    left = {'color': left_color, 'text': left_text, 'width': self.textwidth
        (left_text, config)}
    right = {'color': right_color, 'text': right_text, 'width': self.
        textwidth(right_text, config)}
    template = self.env.get_template(config['template_name'].format(**config))
    return template.render(left=left, right=right, config=config)