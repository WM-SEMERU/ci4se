def read_header(self):
    format = '!HHHHHH'
    length = struct.calcsize(format)
    info = struct.unpack(format, self.data[self.offset:self.offset + length])
    self.offset += length
    self.id = info[0]
    self.flags = info[1]
    self.num_questions = info[2]
    self.num_answers = info[3]
    self.num_authorities = info[4]
    self.num_additionals = info[5]