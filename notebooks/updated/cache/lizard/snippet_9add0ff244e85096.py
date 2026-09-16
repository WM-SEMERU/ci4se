def get_word_list_eng(text):
    words, index = [''], 0
    while index < len(text):
        while index < len(text) and ('a' <= text[index] <= 'z' or 'A' <=
            text[index] <= 'Z'):
            words[-1] += text[index]
            index += 1
        if words[-1]:
            words.append('')
        while index < len(text) and not ('a' <= text[index] <= 'z' or 'A' <=
            text[index] <= 'Z'):
            if text[index] != ' ':
                words[-1] += text[index]
            index += 1
        if words[-1]:
            words.append('')
    if not words[-1]:
        words.pop()
    return words