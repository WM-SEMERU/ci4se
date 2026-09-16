def _reader(path, password, prompt):
    pdf = PdfFileReader(path) if not isinstance(path, PdfFileReader) else path
    if pdf.isEncrypted:
        if not password:
            pdf.decrypt('')
            if pdf.isEncrypted and prompt:
                print('No password has been given for encrypted PDF ', path)
                password = input('Enter Password: ')
            else:
                return False
        pdf.decrypt(password)
    return pdf