def load_file(data_file):
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except JSONDecodeError as e:
        return []