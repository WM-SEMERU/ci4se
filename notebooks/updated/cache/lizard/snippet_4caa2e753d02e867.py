def quotemeta(text):
    text = re.sub('/', '//', text)
    text = re.sub('\\\\{', '/{', text)
    text = re.sub('\\\\}', '/}', text)
    return text