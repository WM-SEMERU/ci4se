def convert_pdf_to_txt(pdf, startpage=None):
    if startpage is not None:
        startpageargs = ['-f', str(startpage)]
    else:
        startpageargs = []
    stdout = subprocess.Popen(['pdftotext', '-q'] + startpageargs + [pdf,
        '-'], stdout=subprocess.PIPE).communicate()[0]
    if not isinstance(stdout, str):
        stdout = stdout.decode()
    return stdout