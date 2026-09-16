def wash_html_id(dirty):
    import re
    if not dirty[0].isalpha():
        dirty = 'i' + dirty
    non_word = re.compile('[^\\w]+')
    return non_word.sub('', dirty)