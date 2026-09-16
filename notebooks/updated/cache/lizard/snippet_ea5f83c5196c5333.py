def hexstr(text):
    text = text.strip().lower()
    if text.startswith(('0x', '0X')):
        text = text[2:]
    if not text:
        raise s_exc.BadTypeValu(valu=text, name='hexstr', mesg=
            'No string left after stripping')
    try:
        s_common.uhex(text)
    except (binascii.Error, ValueError) as e:
        raise s_exc.BadTypeValu(valu=text, name='hexstr', mesg=str(e))
    return text