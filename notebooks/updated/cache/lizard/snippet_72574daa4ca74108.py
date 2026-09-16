def clean(self, text, **kwargs):
    text = stringify(text)
    if text is not None:
        return self.clean_text(text, **kwargs)