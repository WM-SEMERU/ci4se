def calculate_score(search_string, word):
    if len(search_string) > len(word):
        return 0
    original_word = word
    score = 1
    search_index = 0
    while True:
        scale = 1.0
        search_char = search_string[search_index]
        i = word.find(search_char)
        if i < 0:
            return 0
        if i > 0 and word[i - 1] == '-':
            scale = 0.95
        else:
            scale = 1 - i / float(len(word))
        score *= scale
        word = word[i + 1:]
        search_index += 1
        if search_index >= len(search_string):
            break
    completion_scale = 1 - len(word) / float(len(original_word))
    score *= completion_scale
    return score