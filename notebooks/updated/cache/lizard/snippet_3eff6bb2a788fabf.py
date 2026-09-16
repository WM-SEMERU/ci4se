def format_endpoint_argument_doc(argument):
    doc = argument.doc_dict()
    doc['description'] = clean_description(py_doc_trim(doc['description']))
    details = doc.get('detailed_description', None)
    if details is not None:
        doc['detailed_description'] = clean_description(py_doc_trim(details))
    return doc