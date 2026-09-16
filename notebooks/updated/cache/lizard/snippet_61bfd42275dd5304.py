def random_passphrase_from_wordlist(phrase_length, wordlist):
    passphrase_words = []
    numbytes_of_entropy = phrase_length * 2
    entropy = list(dev_random_entropy(numbytes_of_entropy,
        fallback_to_urandom=True))
    bytes_per_word = int(ceil(log(len(wordlist), 2) / 8))
    if phrase_length * bytes_per_word > 64:
        raise Exception(
            'Error! This operation requires too much entropy.             Try a shorter phrase length or word list.'
            )
    for i in range(phrase_length):
        current_entropy = entropy[i * bytes_per_word:(i + 1) * bytes_per_word]
        index = int(''.join(current_entropy).encode('hex'), 16) % len(wordlist)
        word = wordlist[index]
        passphrase_words.append(word)
    return ' '.join(passphrase_words)