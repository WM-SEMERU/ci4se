def soundexCode(self, char):
    lang = get_language(char)
    try:
        if lang == 'en_US':
            return _soundex_map['soundex_en'][charmap[lang].index(char)]
        else:
            return _soundex_map['soundex'][charmap[lang].index(char)]
    except:
        pass
    return 0