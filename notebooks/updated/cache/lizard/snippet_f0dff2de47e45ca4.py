def install(self, tmp_container, font_tmpdir, css_content):
    with open(self.webfont_settings['csspart_path'], 'w') as css_file:
        css_file.write(css_content)
    if os.path.exists(self.webfont_settings['fontdir_path']):
        shutil.rmtree(self.webfont_settings['fontdir_path'])
    font_srcdir = os.path.join(tmp_container, font_tmpdir)
    self._debug('* Installing font')
    self._debug('  - From: {}', font_srcdir)
    self._debug('  - To: {}', self.webfont_settings['fontdir_path'])
    shutil.copytree(font_srcdir, self.webfont_settings['fontdir_path'])
    manifest_src = os.path.join(tmp_container, settings.
        ICOMOON_MANIFEST_FILENAME)
    self._debug('* Installing manifest')
    self._debug('  - From: {}', manifest_src)
    self._debug('  - To: {}', self.webfont_settings['fontdir_path'])
    shutil.copy(manifest_src, self.webfont_settings['fontdir_path'])
    self._debug('* Removing temporary dir')
    shutil.rmtree(tmp_container)