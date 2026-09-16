def set_theme_advanced(self, theme_name, brightness=1.0, saturation=1.0,
    hue=1.0, preserve_transparency=True, output_dir=None, advanced_name=
    'advanced'):
    if not self.png_support:
        raise RuntimeError(
            'PNG-based themes are not supported in the environment')
    if theme_name not in self.pixmap_themes:
        raise ValueError('Theme is not a valid pixmap theme')
    if theme_name not in self.themes:
        raise ValueError('Theme to create new theme from is not available: {}'
            .format(theme_name))
    if advanced_name in self.themes:
        raise RuntimeError(
            'The same name for an advanced theme cannot be used twice')
    output_dir = os.path.join(utils.get_temp_directory(), advanced_name
        ) if output_dir is None else output_dir
    self._setup_advanced_theme(theme_name, output_dir, advanced_name)
    image_directory = os.path.join(output_dir, advanced_name, advanced_name)
    self._setup_images(image_directory, brightness, saturation, hue,
        preserve_transparency)
    with utils.temporary_chdir(output_dir):
        self.tk.call('lappend', 'auto_path', '[{}]'.format(output_dir))
        self.tk.eval('source pkgIndex.tcl')
        self.set_theme(advanced_name)