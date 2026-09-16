def html(cls, string, show_everything=False, translation=gettext.
    NullTranslations()):
    out, _ = tidylib.tidy_fragment(string)
    return out