def formfield(self, **kwargs):
    from yacms.generic.forms import KeywordsWidget
    kwargs['widget'] = KeywordsWidget
    return super(KeywordsField, self).formfield(**kwargs)