def getroot(self):
    if 'class' in self.root.attrib:
        attrib = {'class': self.root.attrib['class']}
    else:
        attrib = None
    return GroupElement(self.root.getchildren(), attrib=attrib)