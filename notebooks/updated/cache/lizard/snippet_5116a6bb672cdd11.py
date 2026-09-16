def from_char(cls, char, name=None, width=None, fill_char=None, bounce=
    False, reverse=False, back_char=None, wrapper=None):
    return cls(cls._generate_move(char, width=width or cls.default_width,
        fill_char=str(fill_char or cls.default_fill_char), bounce=bounce,
        reverse=reverse, back_char=back_char), name=name, wrapper=wrapper or
        cls.default_wrapper)