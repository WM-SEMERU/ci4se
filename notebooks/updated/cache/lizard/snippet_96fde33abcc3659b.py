def lookup_char_from_keycode(self, keycode):
    keysym_index = 0
    if self.modifiers['Num_Lock'] and keycode in self.keypad_keycodes:
        if self.modifiers['Shift'] or self.modifiers['Shift_Lock']:
            keysym_index = 0
        else:
            keysym_index = 1
    elif not self.modifiers['Shift'] and self.modifiers['Caps_Lock']:
        keysym_index = 0
        keysym = self.display.keycode_to_keysym(keycode, keysym_index)
        if keysym & 127 == keysym and chr(keysym
            ) in 'abcdefghijklmnopqrstuvwxyz':
            keysym_index = 1
    elif self.modifiers['Shift'] and self.modifiers['Caps_Lock']:
        keysym_index = 1
        keysym = self.display.keycode_to_keysym(keycode, keysym_index)
        if keysym & 127 == keysym and chr(keysym
            ) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            keysym_index = 0
    elif self.modifiers['Shift'] or self.modifiers['Shift_Lock']:
        keysym_index = 1
    if self.modifiers['Mode_switch']:
        keysym_index += 2
    keysym = self.display.keycode_to_keysym(keycode, keysym_index)
    if keysym & 127 == keysym and self.ascii_printable(keysym):
        return chr(keysym)
    try:
        char = self.keysym_to_string[keysym]
    except KeyError:
        print('Unable to determine character.')
        print('Keycode: {0} KeySym {1}'.format(keycode, keysym))
        return None
    else:
        return char