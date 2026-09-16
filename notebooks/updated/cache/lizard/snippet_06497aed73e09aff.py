def read_ttl(path):
    warnings.warn(
        'Document.read_ttl() is deprecated and will be removed in near future. Use read() instead'
        , DeprecationWarning)
    doc_path = os.path.dirname(path)
    doc_name = os.path.basename(path)
    return Document(doc_name, doc_path).read()