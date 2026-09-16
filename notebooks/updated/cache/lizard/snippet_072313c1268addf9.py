def to_shapefile(output, input_nrml_file, validate):
    input_parser = shapefileparser.SourceModelParser()
    source_model = input_parser.read(input_nrml_file, validate)
    if not output:
        output = os.path.splitext(input_nrml_file)[0]
    print('Extracting %s_ files' % output)
    shapefileparser.ShapefileParser().write(output, source_model)