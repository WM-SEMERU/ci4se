def decryption_statem(self, ciphertext_in, key_in, reset):
    if len(key_in) != len(ciphertext_in):
        raise pyrtl.PyrtlError(
            'AES key and ciphertext should be the same length')
    cipher_text, key = (pyrtl.Register(len(ciphertext_in)) for i in range(2))
    key_exp_in, add_round_in = (pyrtl.WireVector(len(ciphertext_in)) for i in
        range(2))
    reversed_key_list = reversed(self._key_gen(key_exp_in))
    counter = pyrtl.Register(4, 'counter')
    round = pyrtl.WireVector(4)
    counter.next <<= round
    inv_shift = self._inv_shift_rows(cipher_text)
    inv_sub = self._sub_bytes(inv_shift, True)
    key_out = pyrtl.mux(round, *reversed_key_list, default=0)
    add_round_out = self._add_round_key(add_round_in, key_out)
    inv_mix_out = self._mix_columns(add_round_out, True)
    with pyrtl.conditional_assignment:
        with (reset == 1):
            round |= 0
            key.next |= key_in
            key_exp_in |= key_in
            cipher_text.next |= add_round_out
            add_round_in |= ciphertext_in
        with (counter == 10):
            round |= counter
            cipher_text.next |= cipher_text
        with pyrtl.otherwise:
            round |= counter + 1
            key.next |= key
            key_exp_in |= key
            add_round_in |= inv_sub
            with (counter == 9):
                cipher_text.next |= add_round_out
            with pyrtl.otherwise:
                cipher_text.next |= inv_mix_out
    ready = counter == 10
    return ready, cipher_text