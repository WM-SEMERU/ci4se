def _process_assignments(self, anexec, contents, mode='insert'):
    for assign in self.RE_ASSIGN.finditer(contents):
        assignee = assign.group('assignee').strip()
        target = re.split('[(%\\s]', assignee)[0].lower()
        if target in self._intrinsic:
            continue
        if (target in anexec.members or target in anexec.parameters or 
            isinstance(anexec, Function) and target.lower() == anexec.name.
            lower()):
            if mode == 'insert':
                anexec.add_assignment(re.split('[(\\s]', assignee)[0])
            elif mode == 'delete':
                try:
                    index = element.assignments.index(assign)
                    del element.assignments[index]
                except ValueError:
                    pass