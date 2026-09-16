def lpad(s, N, char='\x00'):
    assert isinstance(char, bytes) and len(char
        ) == 1, 'char should be a string with length 1'
    return s.rjust(N, char)