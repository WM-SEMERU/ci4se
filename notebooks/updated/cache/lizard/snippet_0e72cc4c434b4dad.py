def __regions_russian(self, word):
    r1 = ''
    r2 = ''
    rv = ''
    vowels = 'A', 'U', 'E', 'a', 'e', 'i', 'o', 'u', 'y'
    word = word.replace('i^a', 'A').replace('i^u', 'U').replace('e`', 'E')
    for i in range(1, len(word)):
        if word[i] not in vowels and word[i - 1] in vowels:
            r1 = word[i + 1:]
            break
    for i in range(1, len(r1)):
        if r1[i] not in vowels and r1[i - 1] in vowels:
            r2 = r1[i + 1:]
            break
    for i in range(len(word)):
        if word[i] in vowels:
            rv = word[i + 1:]
            break
    r2 = r2.replace('A', 'i^a').replace('U', 'i^u').replace('E', 'e`')
    rv = rv.replace('A', 'i^a').replace('U', 'i^u').replace('E', 'e`')
    return rv, r2