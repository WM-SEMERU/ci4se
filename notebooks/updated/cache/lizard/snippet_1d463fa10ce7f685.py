def build(self, builder):
    params = {}
    if self.lang is not None:
        params['xml:lang'] = self.lang
    builder.start('TranslatedText', params)
    builder.data(self.text)
    builder.end('TranslatedText')