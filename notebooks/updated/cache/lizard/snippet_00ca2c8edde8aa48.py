def _extractErrorString(request):
    errorStr = ''
    tag = None
    try:
        root = ET.fromstring(request.text.encode('utf-8'))
        tag = root[0][0]
    except:
        return errorStr
    for element in tag.getiterator():
        tagName = element.tag.lower()
        if tagName.endswith('string'):
            errorStr += element.text + ' '
        elif tagName.endswith('description'):
            errorStr += element.text + ' '
    return errorStr