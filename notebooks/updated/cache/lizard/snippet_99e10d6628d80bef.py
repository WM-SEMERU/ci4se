def display(self, content=None, **settings):
    lines = self.render(content, **settings)
    for l in lines:
        print(l)