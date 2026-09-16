def _writeContaminantTable(self, session, fileObject, mapTable,
    contaminants, replaceParamFile):
    fileObject.write('%s\n' % mapTable.name)
    fileObject.write('NUM_CONTAM %s\n' % mapTable.numContam)
    for contaminant in contaminants:
        fileObject.write('"%s"  "%s"  %s\n' % (contaminant.name,
            contaminant.indexMap.name, contaminant.outputFilename))
        precipConcString = vwp(contaminant.precipConc, replaceParamFile)
        partitionString = vwp(contaminant.partition, replaceParamFile)
        try:
            precipConc = '%.2f' % precipConcString
        except:
            precipConc = '%s' % precipConcString
        try:
            partition = '%.2f' % partitionString
        except:
            partition = '%s' % partitionString
        fileObject.write('PRECIP_CONC%s%s\n' % (' ' * 10, precipConc))
        fileObject.write('PARTITION%s%s\n' % (' ' * 12, partition))
        fileObject.write('NUM_IDS %s\n' % contaminant.numIDs)
        self._writeValues(session, fileObject, mapTable, contaminant,
            replaceParamFile)