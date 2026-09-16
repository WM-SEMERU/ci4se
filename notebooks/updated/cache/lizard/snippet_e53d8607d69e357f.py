def com_google_fonts_check_mac_style(ttFont, style):
    from fontbakery.utils import check_bit_entry
    from fontbakery.constants import MacStyle
    expected = 'Italic' in style
    yield check_bit_entry(ttFont, 'head', 'macStyle', expected, bitmask=
        MacStyle.ITALIC, bitname='ITALIC')
    expected = style in ['Bold', 'BoldItalic']
    yield check_bit_entry(ttFont, 'head', 'macStyle', expected, bitmask=
        MacStyle.BOLD, bitname='BOLD')