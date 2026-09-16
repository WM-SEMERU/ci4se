def choose(items, title_text, question_text):
    print(title_text)
    for i, item in enumerate(items, start=1):
        print('%d) %s' % (i, item))
    print('%d) Abort' % (i + 1))
    selected = input(question_text)
    try:
        index = int(selected)
    except ValueError:
        index = -1
    if not index - 1 in range(len(items)):
        print('Aborting.')
        return None
    return items[index - 1]