def text_entry(self):
    allowed_sequences = set(['KEY_ENTER', 'KEY_ESCAPE', 'KEY_DELETE'])
    sys.stdout.write('Enter text (<Esc> to abort) : ')
    sys.stdout.flush()
    start_column = self.term.get_location()[1]
    cur_column = start_column
    with self.term.cbreak():
        val = ''
        while val != 'KEY_ENTER' and val != 'KEY_ESCAPE':
            val = self.term.inkey()
            if not val:
                continue
            elif val.is_sequence:
                val = val.name
                if val not in allowed_sequences:
                    continue
            if val == 'KEY_ENTER':
                self.roku.enter()
            elif val == 'KEY_ESCAPE':
                pass
            elif val == 'KEY_DELETE':
                self.roku.backspace()
                if cur_column > start_column:
                    sys.stdout.write('\x08 \x08')
                    cur_column -= 1
            else:
                self.roku.literal(val)
                sys.stdout.write(val)
                cur_column += 1
            sys.stdout.flush()
        sys.stdout.write(self.term.clear_bol)
        sys.stdout.write(self.term.move(self.term.height, 0))
        sys.stdout.flush()