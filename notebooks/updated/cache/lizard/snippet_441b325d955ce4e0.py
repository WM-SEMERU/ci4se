def _read_jsonl(filepath, kwargs):
    with open(filepath) as data_file:
        data = [json.loads(line, **kwargs) for line in data_file if len(
            line) > 0]
    return data