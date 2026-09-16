def wordcount(text):
    bannedwords = read_file('stopwords.txt')
    wordcount = {}
    separated = separate(text)
    for word in separated:
        if word not in bannedwords:
            if not wordcount.has_key(word):
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    return wordcount