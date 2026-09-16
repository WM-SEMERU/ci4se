def _validate_options(self):
    if self.obfuscate_hostname and not self.obfuscate:
        raise ValueError('Option `obfuscate_hostname` requires `obfuscate`')
    if self.analyze_image_id is not None and len(self.analyze_image_id) < 12:
        raise ValueError(
            'Image/Container ID must be at least twelve characters long.')
    if self.enable_schedule and self.disable_schedule:
        raise ValueError(
            'Conflicting options: --enable-schedule and --disable-schedule')
    if self.analyze_container and (self.register or self.unregister):
        raise ValueError(
            'Registration not supported with image or container analysis.')
    if self.to_json and self.to_stdout:
        raise ValueError('Conflicting options: --to-stdout and --to-json')
    if self.payload and not self.content_type:
        raise ValueError('--payload requires --content-type')
    if not self.legacy_upload:
        if self.group:
            raise ValueError('--group is not supported at this time.')
        if self.analyze_image_id:
            raise ValueError(
                '--analyze-image-id is not supported at this time.')
        if self.analyze_file:
            raise ValueError('--analyze-file is not supported at this time.')
        if self.analyze_mountpoint:
            raise ValueError(
                '--analyze-mountpoint is not supported at this time.')
        if self.analyze_container:
            raise ValueError(
                '--analyze-container is not supported at this time.')