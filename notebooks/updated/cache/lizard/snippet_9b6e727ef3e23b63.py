def add_tag(self, tag):
    if tag.replace('@', '') in self.tags:
        return
    self.refresh
    oldContent = self.to_string(indentLevel=1)
    self.tags += [tag.replace('@', '')]
    newContent = self.to_string(indentLevel=1)
    self.parent._update_document_tree(oldContent=oldContent, newContent=
        newContent)
    self.refresh
    return None