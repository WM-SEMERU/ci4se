def _load_data():
    lines = dragonmapper.data.load_data_file('transcriptions.csv')
    pinyin_map, zhuyin_map, ipa_map = {}, {}, {}
    for line in lines:
        p, z, i = line.split(',')
        pinyin_map[p] = {'Zhuyin': z, 'IPA': i}
        zhuyin_map[z] = {'Pinyin': p, 'IPA': i}
        ipa_map[i] = {'Pinyin': p, 'Zhuyin': z}
    return pinyin_map, zhuyin_map, ipa_map