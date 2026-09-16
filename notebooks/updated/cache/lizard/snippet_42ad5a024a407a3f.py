def get_ID_text(token):
    if isinstance(token, CommonToken):
        text = token.text
    else:
        text = token.getText()
    text = text.lstrip('\\')
    return text