def convertforinput(self, filepath, metadata):
    assert isinstance(metadata, CLAMMetaData)
    if not metadata.__class__ in self.acceptforinput:
        raise Exception('Convertor ' + self.__class__.__name__ +
            ' can not convert input files to ' + metadata.__class__.
            __name__ + '!')
    return False