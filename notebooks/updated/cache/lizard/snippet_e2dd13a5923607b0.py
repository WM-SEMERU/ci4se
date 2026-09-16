def standard_program_header(self, title, length, line=32768):
    self.save_header(self.HEADER_TYPE_BASIC, title, length, param1=line,
        param2=length)