def com_google_fonts_check_name_license(ttFont, license):
    from fontbakery.constants import PLACEHOLDER_LICENSING_TEXT
    failed = False
    placeholder = PLACEHOLDER_LICENSING_TEXT[license]
    entry_found = False
    for i, nameRecord in enumerate(ttFont['name'].names):
        if nameRecord.nameID == NameID.LICENSE_DESCRIPTION:
            entry_found = True
            value = nameRecord.toUnicode()
            if value != placeholder:
                failed = True
                yield FAIL, Message('wrong',
                    'License file {} exists but NameID {} (LICENSE DESCRIPTION) value on platform {} ({}) is not specified for that. Value was: "{}" Must be changed to "{}"'
                    .format(license, NameID.LICENSE_DESCRIPTION, nameRecord
                    .platformID, PlatformID(nameRecord.platformID).name,
                    value, placeholder))
    if not entry_found:
        yield FAIL, Message('missing',
            'Font lacks NameID {} (LICENSE DESCRIPTION). A proper licensing entry must be set.'
            .format(NameID.LICENSE_DESCRIPTION))
    elif not failed:
        yield PASS, 'Licensing entry on name table is correctly set.'