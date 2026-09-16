def generate_yaml_file(filename, contents):
    with open(filename, 'w') as file:
        file.write(yaml.dump(contents, default_flow_style=False))