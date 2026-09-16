def secure(pdf, user_pw, owner_pw, restrict_permission=True, pdftk=
    get_pdftk_path(), output=None):
    if pdftk:
        with open(pdf, 'rb') as f:
            reader = PdfFileReader(f)
            if reader.isEncrypted:
                print('PDF is already encrypted')
                return pdf
        if not output:
            output = add_suffix(pdf, 'secured')
        pdf_en = pdf.replace(' ', '\\ ')
        output_en = output.replace(' ', '\\ ')
        command = (pdftk + ' ' + pdf_en + ' output ' + output_en +
            ' owner_pw ' + owner_pw + ' user_pw ' + user_pw)
        if restrict_permission:
            command += ' allow printing'
        os.system(command)
        print('Secured PDF saved to...', output)
        return output
    else:
        print('Unable to locate pdftk binary')