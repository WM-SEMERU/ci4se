def pdfextract_dois(pdf_file):
    references = pdfextract(pdf_file)
    root = ET.fromstring(references)
    plaintext_references = [e.text for e in root.iter('reference')]
    return plaintext.get_cited_dois(plaintext_references)