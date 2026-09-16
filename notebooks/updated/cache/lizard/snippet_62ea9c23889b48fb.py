def pdf_rotate(input: str, counter_clockwise: bool=False, pages: [str]=None,
    output: str=None):
    infile = open(input, 'rb')
    reader = PdfFileReader(infile)
    writer = PdfFileWriter()
    if pages is None:
        source_pages = reader.pages
    else:
        pages = parse_rangearg(pages, len(reader.pages))
        source_pages = [reader.getPage(i) for i in pages]
    for i, page in enumerate(source_pages):
        if pages is None or i in pages:
            if counter_clockwise:
                writer.addPage(page.rotateCounterClockwise(90))
            else:
                writer.addPage(page.rotateClockwise(90))
        else:
            writer.addPage(page)
    if output is None:
        outfile = NamedTemporaryFile(delete=False)
    elif not os.path.isfile(output) or overwrite_dlg(output):
        outfile = open(output, 'wb')
    else:
        return
    writer.write(outfile)
    infile.close()
    outfile.close()
    if output is None:
        if overwrite_dlg(input):
            os.remove(input)
            move(outfile.name, input)
        else:
            os.remove(outfile.name)