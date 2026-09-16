def fix_hunspell_json(badjson_path='en_us.json', goodjson_path=
    'en_us_fixed.json'):
    with open(badjson_path, 'r') as fin:
        with open(goodjson_path, 'w') as fout:
            for i, line in enumerate(fin):
                line2 = regex.sub('\\[(\\w)', '["\\1', line)
                line2 = regex.sub('(\\w)\\]', '\\1"]', line2)
                line2 = regex.sub('(\\w),(\\w)', '\\1","\\2', line2)
                fout.write(line2)
    with open(goodjson_path, 'r') as fin:
        words = []
        with open(goodjson_path + '.txt', 'w') as fout:
            hunspell = json.load(fin)
            for word, affixes in hunspell['words'].items():
                words += [word]
                fout.write(word + '\n')
                for affix in affixes:
                    words += [affix]
                    fout.write(affix + '\n')
    return words