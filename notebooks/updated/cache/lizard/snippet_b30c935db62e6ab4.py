def lang_items(self, lang=None):
    if lang is None:
        lang = self.language
    yield from self.cache.setdefault(lang, {}).items()