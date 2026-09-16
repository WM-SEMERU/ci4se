def add_vtt_file(self, vtt_file, language_type=None):
    if not isinstance(vtt_file, DataInputStream):
        raise InvalidArgument('vtt_file')
    locale = DEFAULT_LANGUAGE_TYPE.identifier
    if language_type is not None:
        locale = language_type.identifier
    self.my_osid_object_form.add_file(vtt_file, locale, asset_name=
        'VTT File Container', asset_description=
        'Used by an asset content to manage multi-language VTT files')