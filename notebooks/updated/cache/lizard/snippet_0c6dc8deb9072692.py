def check(self, url_data):
    content = url_data.get_content()
    filename = get_temp_filename(content)
    try:
        app = get_word_app()
        try:
            doc = open_wordfile(app, filename)
            if doc is None:
                raise Error('could not open word file %r' % filename)
            try:
                for link in doc.Hyperlinks:
                    line = get_line_number(link.Range)
                    name = link.TextToDisplay
                    url_data.add_url(link.Address, name=name, line=line)
            finally:
                close_wordfile(doc)
        finally:
            close_word_app(app)
    except Error as msg:
        log.warn(LOG_PLUGIN, 'Error parsing word file: %s', msg)