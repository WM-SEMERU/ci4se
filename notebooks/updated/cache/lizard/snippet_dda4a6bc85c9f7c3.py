def generate_words(numberofwords, wordlist, secure=None):
    if not secure:
        chooser = random.choice
    else:
        chooser = random.SystemRandom().choice
    return [chooser(wordlist) for _ in range(numberofwords)]