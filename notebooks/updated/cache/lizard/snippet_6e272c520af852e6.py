def get_xpath_root(xpath):
    if xpath:
        if xpath.startswith('@'):
            xpath = ''
        else:
            index = xpath.find('/@' if '@' in xpath else '/{')
            xpath = xpath[:index] if index >= 0 else xpath
    return xpath