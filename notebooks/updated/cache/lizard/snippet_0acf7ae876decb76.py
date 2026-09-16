def _parse_members(self, contents, anexec, params, mode='insert'):
    members = self.vparser.parse(contents, anexec)
    for param in list(params):
        lparam = param.lower()
        if lparam in members:
            if mode == 'insert' and not lparam in anexec.parameters:
                anexec.add_parameter(members[lparam])
            elif mode == 'delete':
                anexec.remove_parameter(members[lparam])
    for key in members:
        if mode == 'insert':
            if not key.lower() in anexec.parameters:
                anexec.members[key] = members[key]
        elif mode == 'delete' and key in anexec.members:
            del anexec.members[key]
    if mode == 'insert':
        memdocs = self.docparser.parse_docs(contents, anexec)
        if anexec.name in memdocs:
            docs = self.docparser.to_doc(memdocs[anexec.name][0], anexec.name)
            self.docparser.process_memberdocs(docs, anexec)
        self.docparser.process_embedded(memdocs, anexec)