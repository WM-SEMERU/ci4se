def parse_inline(self):
    if self.inline_children:
        self.children = parser.parse_inline(self.children)
    elif isinstance(getattr(self, 'children', None), list):
        for child in self.children:
            if isinstance(child, BlockElement):
                child.parse_inline()