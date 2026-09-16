def _output_path(self, ufo_or_font_name, ext, is_instance=False,
    interpolatable=False, autohinted=False, is_variable=False, output_dir=
    None, suffix=None):
    if isinstance(ufo_or_font_name, basestring):
        font_name = ufo_or_font_name
    elif ufo_or_font_name.path:
        font_name = os.path.splitext(os.path.basename(os.path.normpath(
            ufo_or_font_name.path)))[0]
    else:
        font_name = self._font_name(ufo_or_font_name)
    if output_dir is None:
        output_dir = self._output_dir(ext, is_instance, interpolatable,
            autohinted, is_variable)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if suffix:
        return os.path.join(output_dir, '{}-{}.{}'.format(font_name, suffix,
            ext))
    else:
        return os.path.join(output_dir, '{}.{}'.format(font_name, ext))