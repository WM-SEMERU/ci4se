def com_google_fonts_check_metadata_valid_post_script_name_values(font_metadata
    , font_familynames):
    for font_familyname in font_familynames:
        psname = ''.join(str(font_familyname).split())
        if psname in ''.join(font_metadata.post_script_name.split('-')):
            yield PASS, 'METADATA.pb postScriptName field contains font name in right format.'
        else:
            yield FAIL, 'METADATA.pb postScriptName ("{}") does not match correct font name format ("{}").'.format(
                font_metadata.post_script_name, font_familyname)