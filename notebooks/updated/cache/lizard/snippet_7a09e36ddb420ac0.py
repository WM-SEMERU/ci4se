def isolate(obj):
    answers = []
    for token in obj:
        lemmata = token[1]
        for pair in lemmata:
            answers.append(pair[0])
    return answers