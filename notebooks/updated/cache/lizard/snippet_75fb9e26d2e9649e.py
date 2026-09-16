def _repr_html_(self, **kwargs):
    from jinja2 import Template
    from markdown import markdown as convert_markdown
    extensions = ['markdown.extensions.extra', 'markdown.extensions.admonition'
        ]
    return convert_markdown(self.markdown, extensions)