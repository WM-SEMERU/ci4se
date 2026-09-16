def handle_typical_memberdefs_no_overload(self, signature, memberdef_nodes):
    for n in memberdef_nodes:
        self.add_text(['\n', '%feature("docstring") ', signature, ' "', '\n'])
        if self.with_function_signature:
            self.add_line_with_subsequent_indent(self.get_function_signature(n)
                )
        self.subnode_parse(n, pieces=[], ignore=['definition', 'name'])
        self.add_text(['";', '\n'])