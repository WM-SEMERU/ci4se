def pseudolocalizefile(self, input_filename, output_filename,
    input_encoding='UTF-8', output_encoding='UTF-8', overwrite_existing=True):
    leading_trailing_double_quotes = re.compile('^"|"$')
    if not os.path.isfile(input_filename):
        raise IOError('Input message catalog not found: {0}'.format(os.path
            .abspath(input_filename)))
    if os.path.isfile(output_filename) and not overwrite_existing:
        raise IOError('Error, output message catalog already exists: {0}'.
            format(os.path.abspath(output_filename)))
    with codecs.open(input_filename, mode='r', encoding=input_encoding
        ) as in_fileobj:
        with codecs.open(output_filename, mode='w', encoding=output_encoding
            ) as out_fileobj:
            for current_line in in_fileobj:
                out_fileobj.write(current_line)
                if current_line.startswith('msgid'):
                    msgid = current_line.split(None, 1)[1].strip()
                    msgid = leading_trailing_double_quotes.sub('', msgid)
                    msgstr = self.l10nutil.pseudolocalize(msgid)
                    out_fileobj.write('msgstr "{0}"\n'.format(msgstr))
                    next(in_fileobj)