def search(document, search):
    result = False
    searchre = re.compile(search)
    for element in document.iter():
        if element.tag == '{%s}t' % nsprefixes['w']:
            if element.text:
                if searchre.search(element.text):
                    result = True
    return result