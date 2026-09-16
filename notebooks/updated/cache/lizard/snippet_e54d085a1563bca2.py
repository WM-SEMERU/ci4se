def walk(self, listener):
    antlr4.ParseTreeWalker.DEFAULT.walk(listener, self.__parse_tree)