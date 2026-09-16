def import_doc(self, file_uris, docsearch, current_doc=None):
    doc = None
    docs = []
    pages = []
    file_uris = [self.fs.safe(uri) for uri in file_uris]
    imported = []
    for file_uri in file_uris:
        logger.info("Importing PDF from '%s'" % file_uri)
        idx = 0
        for child in self.fs.recurse(file_uri):
            gc.collect()
            if not self.check_file_type(child):
                continue
            h = PdfDoc.hash_file(self.fs, child)
            if docsearch.is_hash_in_index(h):
                logger.info('Document %s already found in the index. Skipped',
                    child)
                continue
            imported.append(child)
            doc = PdfDoc(self.fs, docsearch.rootdir)
            error = doc.import_pdf(child)
            if error:
                continue
            docs.append(doc)
            pages += [p for p in doc.pages]
            idx += 1
    return ImportResult(imported_file_uris=imported, select_doc=doc,
        new_docs=docs, new_docs_pages=pages, stats={_('PDF'): len(docs), _(
        'Document(s)'): len(docs), _('Page(s)'): sum([d.nb_pages for d in
        docs])})