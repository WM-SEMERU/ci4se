def convertTranscriptEffect(self, annStr, hgvsG):
    effect = self._createGaTranscriptEffect()
    effect.hgvs_annotation.CopyFrom(protocol.HGVSAnnotation())
    annDict = dict()
    if self._annotationType == ANNOTATIONS_SNPEFF:
        annDict = dict(zip(self.SNPEFF_FIELDS, annStr.split('|')))
    elif self._annotationType == ANNOTATIONS_VEP_V82:
        annDict = dict(zip(self.VEP_FIELDS, annStr.split('|')))
    else:
        annDict = dict(zip(self.CSQ_FIELDS, annStr.split('|')))
    annDict['hgvs_annotation.genomic'] = hgvsG if hgvsG else ''
    for key, val in annDict.items():
        try:
            protocol.deepSetAttr(effect, key, val)
        except AttributeError:
            if val and key not in self.EXCLUDED_FIELDS:
                protocol.setAttribute(effect.attributes.attr[key].values, val)
    effect.effects.extend(self.convertSeqOntology(annDict.get('effects')))
    self.addLocations(effect, annDict.get('protPos'), annDict.get('cdnaPos'))
    effect.id = self.getTranscriptEffectId(effect)
    return effect