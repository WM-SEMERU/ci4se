def convert_to_namespace(file, output, keyword):
    resource = parse_bel_resource(file)
    write_namespace(namespace_keyword=keyword or resource[
        'AnnotationDefinition']['Keyword'], namespace_name=resource[
        'AnnotationDefinition']['Keyword'], namespace_description=resource[
        'AnnotationDefinition']['DescriptionString'], author_name=
        'Charles Tapley Hoyt', namespace_domain=NAMESPACE_DOMAIN_OTHER,
        values=resource['Values'], citation_name=resource['Citation'][
        'NameString'], file=output)