def lemmatize(text_string):
    if text_string is None or text_string == '':
        return ''
    elif isinstance(text_string, str):
        return LEMMATIZER.lemmatize(text_string)
    else:
        raise InputError('string not passed as primary argument')