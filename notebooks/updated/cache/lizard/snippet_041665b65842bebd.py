def setErrorHandler(self, f, arg):
    libxml2mod.xmlParserCtxtSetErrorHandler(self._o, f, arg)