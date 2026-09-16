def saveXml(self, xml):
    lvls = []
    for logger, level in self.loggerLevels().items():
        lvls.append('{0}:{1}'.format(logger, level))
    xlevels = ElementTree.SubElement(xml, 'levels')
    xlevels.text = ','.join(map(str, self.activeLevels()))
    xloggerlevels = ElementTree.SubElement(xml, 'logger_levels')
    xloggerlevels.text = ','.join(lvls)
    xml.set('filter', wrapVariant(self.uiFilterTXT.text()))
    xtree = ElementTree.SubElement(xml, 'tree')
    self.uiRecordTREE.saveXml(xtree)