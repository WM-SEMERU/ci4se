def docs(node, manifest, config, column_name=None):
    current_project = config.project_name

    def do_docs(*args):
        if len(args) == 1:
            doc_package_name = None
            doc_name = args[0]
        elif len(args) == 2:
            doc_package_name, doc_name = args
        else:
            dbt.exceptions.doc_invalid_args(node, args)
        target_doc = ParserUtils.resolve_doc(manifest, doc_name,
            doc_package_name, current_project, node.package_name)
        if target_doc is None:
            dbt.exceptions.doc_target_not_found(node, doc_name,
                doc_package_name)
        return target_doc.block_contents
    return do_docs