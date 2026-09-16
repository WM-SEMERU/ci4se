def visit_image(self, node):
    uri = node.attributes['uri']
    doc_folder = os.path.dirname(self.builder.current_docname)
    if uri.startswith(doc_folder):
        uri = uri[len(doc_folder):]
        if uri.startswith('/'):
            uri = '.' + uri
    self.add('\n\n![image](%s)\n\n' % uri)