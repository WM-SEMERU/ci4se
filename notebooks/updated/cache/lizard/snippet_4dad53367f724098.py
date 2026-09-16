def __remove_duplicate_and_problematic_analyses(self, docs):
    for doc in docs:
        for word in doc[WORDS]:
            toDelete = []
            for i in range(len(word[ANALYSIS])):
                if i + 1 < len(word[ANALYSIS]):
                    for j in range(i + 1, len(word[ANALYSIS])):
                        analysisI = word[ANALYSIS][i]
                        analysisJ = word[ANALYSIS][j]
                        if self.__analyses_match(analysisI, analysisJ):
                            if j not in toDelete:
                                toDelete.append(j)
            if toDelete:
                for a in sorted(toDelete, reverse=True):
                    del word[ANALYSIS][a]
            if any([(a[POSTAG] == 'V' and a[ENDING] == 'tama') for a in
                word[ANALYSIS]]) and any([(a[POSTAG] == 'V' and a[ENDING] ==
                'ma') for a in word[ANALYSIS]]):
                toDelete = []
                for a in range(len(word[ANALYSIS])):
                    if word[ANALYSIS][a][POSTAG] == 'V' and word[ANALYSIS][a][
                        ENDING] == 'tama':
                        toDelete.append(a)
                if toDelete:
                    for a in sorted(toDelete, reverse=True):
                        del word[ANALYSIS][a]