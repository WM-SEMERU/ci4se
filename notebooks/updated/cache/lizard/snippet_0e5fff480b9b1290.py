def write_json(template, file_name='../dxf.json.template'):
    with open(file_name, 'w') as f:
        json.dump(template, f, indent=4)