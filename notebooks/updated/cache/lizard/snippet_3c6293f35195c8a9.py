def setup_top(self):
    self.top_grammar = SchemaNode('grammar')
    self.top_grammar.attr = {'xmlns': 'http://relaxng.org/ns/structure/1.0',
        'datatypeLibrary': 'http://www.w3.org/2001/XMLSchema-datatypes'}
    self.tree = SchemaNode('start')