def fix_text_segment(text, *, fix_entities='auto', remove_terminal_escapes=
    True, fix_encoding=True, fix_latin_ligatures=True, fix_character_width=
    True, uncurl_quotes=True, fix_line_breaks=True, fix_surrogates=True,
    remove_control_chars=True, remove_bom=True, normalization='NFC'):
    if isinstance(text, bytes):
        raise UnicodeError(fixes.BYTES_ERROR_TEXT)
    if fix_entities == 'auto' and '<' in text and '>' in text:
        fix_entities = False
    while True:
        origtext = text
        if remove_terminal_escapes:
            text = fixes.remove_terminal_escapes(text)
        if fix_encoding:
            text = fixes.fix_encoding(text)
        if fix_entities:
            text = fixes.unescape_html(text)
        if fix_latin_ligatures:
            text = fixes.fix_latin_ligatures(text)
        if fix_character_width:
            text = fixes.fix_character_width(text)
        if uncurl_quotes:
            text = fixes.uncurl_quotes(text)
        if fix_line_breaks:
            text = fixes.fix_line_breaks(text)
        if fix_surrogates:
            text = fixes.fix_surrogates(text)
        if remove_control_chars:
            text = fixes.remove_control_chars(text)
        if remove_bom and not remove_control_chars:
            text = fixes.remove_bom(text)
        if normalization is not None:
            text = unicodedata.normalize(normalization, text)
        if text == origtext:
            return text