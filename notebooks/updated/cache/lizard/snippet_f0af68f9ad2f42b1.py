def add_task(self, title, tags=None):
    self.refresh
    task = title.strip()
    if task[:2] != '- ':
        task = '- ' + task
    if tags:
        if isinstance(tags, list):
            if '@' not in tags[0]:
                tagString = ' @'.join(tags)
                tagString = '@' + tagString
            else:
                tagString = ' '.join(tags)
        else:
            tagString = tags
        tagString = tagString.strip()
        task += ' ' + tagString
    newTask = self._get_object(regex=re.compile(
        '((?<=\\n)|(?<=^))(?P<title>- ((?! @).)*)( *(?P<tagString>( *?@[^(\\s]+(\\([^)]*\\))?)+))?(?P<content>(\\n(( |\\t)+\\S.*)|\\n( |\\t)*)*)'
        , re.UNICODE), objectType='task', content=task)
    oldContent = self.to_string(indentLevel=1)
    newContent = self.to_string(indentLevel=1, tasks=self.tasks + newTask)
    if self.parent:
        doc = self.parent._update_document_tree(oldContent=oldContent,
            newContent=newContent)
    self.content = self.content.replace(self.to_string(indentLevel=0, title
        =False), self.to_string(indentLevel=0, title=False, tasks=self.
        tasks + newTask))
    doc = self
    while doc.parent:
        doc = doc.parent
    doc.refresh
    if not self.parent:
        parent = self
    else:
        parent = doc.get_project(self.title)
    if not parent:
        parent = doc.get_task(self.title)
    thisTask = parent.get_task(title)
    self.refresh
    return thisTask