def generate(schema_file, all_options):
    schema = load_schema_file(open(schema_file, 'r'))
    config_parser = generate_config_parser(schema, include_all=all_options)
    config_parser.write(sys.stdout)