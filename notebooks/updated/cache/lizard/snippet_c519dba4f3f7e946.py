def write_document(self, name, document):
    with open(name, 'wb') as out:
        out.write(etree.tostring(document, encoding='utf-8', pretty_print=True)
            )