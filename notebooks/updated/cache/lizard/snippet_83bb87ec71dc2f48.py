def com_adobe_fonts_check_name_postscript_vs_cff(ttFont):
    failed = False
    cff_names = ttFont['CFF '].cff.fontNames
    if len(cff_names) != 1:
        yield ERROR, 'Unexpected number of font names in CFF table.'
        return
    cff_name = cff_names[0]
    for entry in ttFont['name'].names:
        if entry.nameID == NameID.POSTSCRIPT_NAME:
            postscript_name = entry.toUnicode()
            if postscript_name != cff_name:
                yield FAIL, "Name table PostScript name '{}' does not match CFF table FontName '{}'.".format(
                    postscript_name, cff_name)
                failed = True
    if not failed:
        yield PASS, 'Name table PostScript name matches CFF table FontName.'