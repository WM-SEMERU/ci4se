def getItalianAccentedVocal(vocal, acc_type='g'):
    vocals = {'a': {'g': 'à', 'a': 'á'}, 'e': {'g': 'è', 'a': 'é'}, 'i': {
        'g': 'ì', 'a': 'í'}, 'o': {'g': 'ò', 'a': 'ó'}, 'u': {'g': 'ù', 'a':
        'ú'}}
    return vocals[vocal][acc_type]