def cget(self, key):
    if key == 'headertext':
        return self.__headertext
    elif key == 'text':
        return self.__text
    elif key == 'width':
        return self.__width
    elif key == 'timeout':
        return self._timeout
    elif key == 'background':
        return self.__background
    else:
        return ttk.Frame.cget(self, key)