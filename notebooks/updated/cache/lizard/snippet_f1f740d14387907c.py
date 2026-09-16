def performXpath(parent, xpath):
    loop = False
    if xpath.startswith('.//'):
        result = parent.xpath(xpath.replace('.//', './', 1), namespaces=
            XPATH_NAMESPACES)
        if len(result) == 0:
            result = parent.xpath('*[{}]'.format(xpath), namespaces=
                XPATH_NAMESPACES)
            loop = True
    else:
        result = parent.xpath(xpath, namespaces=XPATH_NAMESPACES)
    return result[0], loop