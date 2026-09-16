def chunked(sentence):
    chunks = []
    for word in sentence:
        if word.chunk is not None:
            if len(chunks) == 0 or chunks[-1] != word.chunk:
                chunks.append(word.chunk)
        else:
            ch = Chink(sentence)
            ch.append(word.copy(ch))
            chunks.append(ch)
    return chunks