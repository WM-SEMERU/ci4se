def write_pdf(pdf_obj, destination):
    reader = PdfFileReader(pdf_obj)
    writer = PdfFileWriter()
    page_count = reader.getNumPages()
    for page_number in range(page_count):
        page = reader.getPage(page_number)
        writer.addPage(page)
    with open(destination, 'wb') as outputStream:
        writer.write(outputStream)