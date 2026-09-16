def convert_to_unicode(tscii_input):
    output = list()
    prev = None
    prev2x = None
    for char in tscii_input:
        if ord(char) < 128:
            output.append(char)
            prev = None
            prev2x = None
        elif ord(char) in ISCII_DIRECT_LOOKUP:
            if prev in ISCII_PRE_MODIFIER:
                curr_char = [ISCII[ord(char)], ISCII[prev]]
            else:
                curr_char = [ISCII[ord(char)]]
                char = None
            output.extend(curr_char)
        elif ord(char) in ISCII_POST_MODIFIER:
            if prev in ISCII_DIRECT_LOOKUP and prev2x in ISCII_PRE_MODIFIER:
                if len(output) >= 2:
                    del output[-1]
                    del output[-2]
                elif len(output) == 1:
                    del output[-1]
                else:
                    pass
                output.extend([ISCII[prev], ISCII[prev2x]])
            else:
                print(
                    'Warning: malformed ISCII encoded file; skipping characters'
                    )
            prev = None
            char = None
        else:
            pass
        prev2x = prev
        if char:
            prev = ord(char)
    return ''.join(output)