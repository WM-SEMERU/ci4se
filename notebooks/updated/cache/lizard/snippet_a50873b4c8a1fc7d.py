def write(self, fptr):
    length = 8 + len(self.label.encode())
    fptr.write(struct.pack('>I4s', length, b'lbl '))
    fptr.write(self.label.encode())