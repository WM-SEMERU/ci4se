def peek_char(self, lpBaseAddress):
    char = self.peek(lpBaseAddress, 1)
    if char:
        return ord(char)
    return 0