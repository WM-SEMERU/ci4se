def _build_word(syl, vowels):
    return "(?:{syl}(?:-(?={syl})|'(?=[{a}{e}{o}])(?={syl}))?)+".format(syl
        =syl, a=vowels['a'], e=vowels['e'], o=vowels['o'])