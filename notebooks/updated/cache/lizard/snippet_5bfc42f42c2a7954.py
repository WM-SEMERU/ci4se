def downloadMARCOAI(doc_id, base):
    downer = Downloader()
    data = downer.download(ALEPH_URL + Template(OAI_DOC_URL_TEMPLATE).
        substitute(DOC_ID=doc_id, BASE=base))
    dom = dhtmlparser.parseString(data)
    error = dom.find('error')
    if len(error) <= 0:
        return data
    if 'Error reading document' in error[0].getContent():
        raise DocumentNotFoundException(str(error[0].getContent()))
    else:
        raise InvalidAlephBaseException(error[0].getContent() + '\n' +
            "The base you are trying to access probably doesn't exist.")