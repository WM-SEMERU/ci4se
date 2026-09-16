def tag_syntax_maltparser(self):
    if not self.__syntactic_parser or not isinstance(self.
        __syntactic_parser, MaltParser):
        self.__syntactic_parser = MaltParser()
    return self.tag_syntax()