def get_language_info(language):
    language = Language.get(language)
    language_full = language.maximize()
    info = {'script': language_full.script, 'tokenizer': 'regex',
        'normal_form': 'NFKC', 'remove_marks': False, 'dotless_i': False,
        'diacritics_under': None, 'transliteration': None,
        'lookup_transliteration': None}
    if _language_in_list(language, ['ja', 'ko']):
        info['tokenizer'] = 'mecab'
    elif _language_in_list(language, ['zh', 'yue']):
        info['tokenizer'] = 'jieba'
    elif info['script'] in SPACELESS_SCRIPTS:
        info['tokenizer'] = None
    if info['script'] in ['Latn', 'Grek', 'Cyrl']:
        info['normal_form'] = 'NFC'
    if info['script'] in ['Arab', 'Hebr']:
        info['remove_marks'] = True
    if _language_in_list(language, ['tr', 'az', 'kk']):
        info['dotless_i'] = True
        info['diacritics_under'] = 'cedillas'
    elif _language_in_list(language, ['ro']):
        info['diacritics_under'] = 'commas'
    if _language_in_list(language, ['sr']):
        info['transliteration'] = 'sr-Latn'
    elif _language_in_list(language, ['az']):
        info['transliteration'] = 'az-Latn'
    if language.language == 'zh' and language.script != 'Hant':
        info['lookup_transliteration'] = 'zh-Hans'
    return info