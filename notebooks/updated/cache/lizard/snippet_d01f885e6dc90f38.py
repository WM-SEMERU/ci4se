def _handle_content(self, relpath, params):
    abspath = os.path.normpath(os.path.join(self._root, relpath))
    if os.path.isfile(abspath):
        with open(abspath, 'rb') as infile:
            content = infile.read()
    else:
        content = 'No file found at {}'.format(abspath).encode('utf-8')
    content_type = mimetypes.guess_type(abspath)[0] or 'text/plain'
    if not content_type.startswith('text/'
        ) and not content_type == 'application/xml':
        n = 120
        content = repr(content)[1:-1]
        content = '\n'.join([content[i:i + n] for i in range(0, len(content
            ), n)])
        prettify = False
        prettify_extra_langs = []
    else:
        prettify = True
        if self._settings.assets_dir:
            prettify_extra_dir = os.path.join(self._settings.assets_dir,
                'js', 'prettify_extra_langs')
            prettify_extra_langs = [{'name': x} for x in os.listdir(
                prettify_extra_dir)]
        else:
            prettify_extra_langs = []
    linenums = True
    args = {'prettify_extra_langs': prettify_extra_langs, 'content':
        content, 'prettify': prettify, 'linenums': linenums}
    content = self._renderer.render_name('file_content.html', args).encode(
        'utf-8')
    self._send_content(content, 'text/html')