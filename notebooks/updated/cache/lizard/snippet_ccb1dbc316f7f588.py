def pdf_add(dest: str, source: str, pages: [str], output: str):
    if output is not None and os.path.isfile(output):
        if not overwrite_dlg(output):
            return
    writer = PdfFileWriter()
    destfile = open(dest, 'rb')
    destreader = PdfFileReader(destfile)
    for page in destreader.pages:
        writer.addPage(page)
    srcfile = open(source, 'rb')
    srcreader = PdfFileReader(srcfile)
    if pages is None:
        for i, page in enumerate(srcreader.pages):
            writer.addPage(page)
    else:
        pages = parse_rangearg(pages, len(srcreader.pages))
        for pagenr in pages:
            page = srcreader.getPage(pagenr)
            writer.addPage(page)
    if output is None:
        if overwrite_dlg(dest):
            tempfile = NamedTemporaryFile(delete=False)
            writer.write(tempfile)
            tempfile.close()
            destfile.close()
            srcfile.close()
            os.remove(dest)
            move(tempfile.name, dest)
    else:
        with open(output, 'wb') as outfile:
            writer.write(outfile)
            destfile.close()
            srcfile.close()