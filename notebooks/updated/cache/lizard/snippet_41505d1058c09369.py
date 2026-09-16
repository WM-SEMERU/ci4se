def open_json(file_name):
    with open(file_name, 'r') as json_data:
        data = json.load(json_data)
        return data