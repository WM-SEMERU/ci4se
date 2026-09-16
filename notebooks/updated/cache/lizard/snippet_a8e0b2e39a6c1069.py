def encipher_shift(plaintext, plain_vocab, shift):
    ciphertext = []
    cipher = ShiftEncryptionLayer(plain_vocab, shift)
    for _, sentence in enumerate(plaintext):
        cipher_sentence = []
        for _, character in enumerate(sentence):
            encrypted_char = cipher.encrypt_character(character)
            cipher_sentence.append(encrypted_char)
        ciphertext.append(cipher_sentence)
    return ciphertext