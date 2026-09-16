def set_string_value(self, index, s):
    return self.__set_string_value(index, javabridge.get_env().new_string(s))