def import_doc(self, file_uris, docsearch, current_doc=None):
    if current_doc is None or current_doc.is_new or not current_doc.can_edit:
        if not current_doc or not current_doc.can_edit:
            current_doc = ImgDoc(self.fs, docsearch.rootdir)
        new_docs = [current_doc]
        upd_docs = []
    else:
        new_docs = []
        upd_docs = [current_doc]
    new_docs_pages = []
    upd_docs_pages = []
    page = None
    file_uris = natsorted(file_uris)
    imported = []
    for file_uri in file_uris:
        file_uri = self.fs.safe(file_uri)
        logger.info("Importing images from '%s'" % file_uri)
        for child in self.fs.recurse(file_uri):
            if '.thumb.' in child:
                logger.info('{} ignored'.format(child))
                continue
            if not self.check_file_type(child):
                continue
            imported.append(child)
            with self.fs.open(child, 'rb') as fd:
                img = Image.open(fd)
                img.load()
            page = current_doc.add_page(img, [])
            if new_docs == []:
                upd_docs_pages.append(page)
            else:
                new_docs_pages.append(page)
    return ImportResult(imported_file_uris=imported, select_doc=current_doc,
        select_page=page, new_docs=new_docs, upd_docs=upd_docs,
        new_docs_pages=new_docs_pages, upd_docs_pages=upd_docs_pages, stats
        ={_('Image file(s)'): len(file_uris), _('Document(s)'): 0 if 
        new_docs == [] else 1, _('Page(s)'): len(new_docs_pages) + len(
        upd_docs_pages)})