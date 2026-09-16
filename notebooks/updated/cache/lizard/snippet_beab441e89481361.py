def xml_endtag(self, name):
    self.level -= 1
    assert self.level >= 0
    self.write(self.indent * self.level)
    self.writeln('</%s>' % xmlquote(name))