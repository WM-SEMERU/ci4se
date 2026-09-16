def encryption(self, plaintext, key):
    if len(plaintext) != self._key_len:
        raise pyrtl.PyrtlError('Ciphertext length is invalid')
    if len(key) != self._key_len:
        raise pyrtl.PyrtlError('key length is invalid')
    key_list = self._key_gen(key)
    t = self._add_round_key(plaintext, key_list[0])
    for round in range(1, 11):
        t = self._sub_bytes(t)
        t = self._shift_rows(t)
        if round != 10:
            t = self._mix_columns(t)
        t = self._add_round_key(t, key_list[round])
    return t