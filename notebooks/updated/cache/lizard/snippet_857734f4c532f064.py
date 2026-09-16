def pre_disambiguate(self, docs):
    lexicon = self.__create_proper_names_lexicon(docs)
    self.__disambiguate_proper_names_1(docs, lexicon)
    certainNames = self.__find_certain_proper_names(docs)
    sentInitialNames = self.__find_sentence_initial_proper_names(docs)
    sentCentralNames = self.__find_sentence_central_proper_names(docs)
    onlySentenceInitial = sentInitialNames.difference(sentCentralNames)
    notProperNames = onlySentenceInitial.difference(certainNames)
    if len(notProperNames) > 0:
        self.__remove_redundant_proper_names(docs, notProperNames)
    lexicon = self.__create_proper_names_lexicon(docs)
    self.__disambiguate_proper_names_2(docs, lexicon)
    return docs