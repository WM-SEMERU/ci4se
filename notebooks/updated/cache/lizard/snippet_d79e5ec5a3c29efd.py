def json2file(data, filename, encoding='utf-8'):
    with codecs.open(filename, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)