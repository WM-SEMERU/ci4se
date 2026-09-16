def workbook_data(self):
    document = XML(fn=os.path.splitext(self.fn)[0] + '.xml', root=Element.
        workbook())
    shared_strings = [str(t.text) for t in self.xml('xl/sharedStrings.xml')
        .root.xpath('.//xl:t', namespaces=self.NS)]
    for key in self.sheets.keys():
        worksheet = self.sheets[key].transform(XT, shared_strings=
            shared_strings)
        document.root.append(worksheet.root)
    return document