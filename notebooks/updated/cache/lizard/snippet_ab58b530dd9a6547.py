def com_google_fonts_check_metadata_valid_name_values(style, font_metadata,
    font_familynames, typographic_familynames):
    from fontbakery.constants import RIBBI_STYLE_NAMES
    if style in RIBBI_STYLE_NAMES:
        familynames = font_familynames
    else:
        familynames = typographic_familynames
    failed = False
    for font_familyname in familynames:
        if font_familyname not in font_metadata.name:
            failed = True
            yield FAIL, 'METADATA.pb font.name field ("{}") does not match correct font name format ("{}").'.format(
                font_metadata.name, font_familyname)
    if not failed:
        yield PASS, 'METADATA.pb font.name field contains font name in right format.'