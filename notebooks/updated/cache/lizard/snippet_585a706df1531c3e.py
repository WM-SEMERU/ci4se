def end(self):
    if self.lastUrl is not None:
        self.html.write('</li>\n')
    if self.lastComic is not None:
        self.html.write('</ul>\n')
    self.html.write('</ul>\n')
    self.addNavLinks()
    self.html.close()