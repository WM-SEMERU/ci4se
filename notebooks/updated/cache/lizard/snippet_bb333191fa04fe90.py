def com_google_fonts_check_family_panose_proportion(ttFonts):
    failed = False
    proportion = None
    for ttFont in ttFonts:
        if proportion is None:
            proportion = ttFont['OS/2'].panose.bProportion
        if proportion != ttFont['OS/2'].panose.bProportion:
            failed = True
    if failed:
        yield FAIL, 'PANOSE proportion is not the same accross this family. In order to fix this, please make sure that the panose.bProportion value is the same in the OS/2 table of all of this family font files.'
    else:
        yield PASS, 'Fonts have consistent PANOSE proportion.'