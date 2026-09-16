def del_tag(self, tag):
    if tag.replace('@', '') not in self.tags:
        return
    self.refresh
    oldContent = self.to_string(indentLevel=1)
    newTags = []
    newTags[:] = [n for n in newTags if tag not in n]
    self.tags = newTags
    newContent = self.to_string(indentLevel=1)
    self.parent._update_document_tree(oldContent=oldContent, newContent=
        newContent)
    self.refresh
    return None