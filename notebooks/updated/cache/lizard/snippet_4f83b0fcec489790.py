def abook_file(vcard, bookfile):
    book = ConfigParser(default_section='format')
    book['format'] = {}
    book['format']['program'] = 'abook'
    book['format']['version'] = '0.6.1'
    for i, card in enumerate(readComponents(vcard.read())):
        Abook.to_abook(card, str(i), book, bookfile)
    with open(bookfile, 'w') as fp:
        book.write(fp, False)