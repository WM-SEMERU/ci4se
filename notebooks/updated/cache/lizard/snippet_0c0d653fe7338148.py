def read_kw_file():
    self_path = os.path.dirname(__file__)
    kw_list_path = join(self_path, '../templates/keyword_list.json.bz2')
    with bz2.BZ2File(kw_list_path) as f:
        kw_list = f.read()
    return json.loads(kw_list)