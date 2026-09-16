def getLemmatization(self, fullPOSTag=False):
    leaves = self._getTreeLeaves()
    lemmas = {}
    for leaf in leaves:
        analyses = []
        if 'analysis_list' in leaf.keys():
            for analysis in leaf['analysis_list']:
                analyses.append({'lemma': analysis['lemma'], 'pos': 
                    analysis['tag'] if fullPOSTag else analysis['tag'][:2]})
        lemmas[leaf['form']] = analyses
    return lemmas