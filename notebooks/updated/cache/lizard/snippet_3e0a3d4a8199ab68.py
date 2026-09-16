def grepPDF(self, path):
    with open(path, 'rb') as pdf_file_obj:
        match = set()
        text = ''
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        pages = pdf_reader.numPages
        for page in range(pages):
            page_obj = pdf_reader.getPage(page)
            text += '\n' + page_obj.extractText()
        match.update(set(x.lower() for x in re.findall(self._keywords, text,
            re.IGNORECASE)))
    return match