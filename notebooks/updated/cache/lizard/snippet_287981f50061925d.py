def name(self, decl_string):
    if not self.has_pattern(decl_string):
        return decl_string
    args_begin = decl_string.find(self.__begin)
    return decl_string[0:args_begin].strip()