def cli(yamlfile, format, output):
    print(OwlSchemaGenerator(yamlfile, format).serialize(output=output))