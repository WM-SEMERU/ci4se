def decrypt(key, ciphertext, shift_function=shift_case_english):
    return [shift_function(key, symbol) for symbol in ciphertext]