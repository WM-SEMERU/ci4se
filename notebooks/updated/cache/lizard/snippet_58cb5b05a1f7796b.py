def get_best_answer(self, query):
    query = to_unicode(query)
    session = self.Session()
    grams = self._get_grams(session, query)
    if not grams:
        raise NoAnswerError('Can not found answer')
    documents = set([doc for gram in grams for doc in gram.documents])
    self._recalc_idfs(session, grams)
    idfs = dict((gram.gram, gram.idf) for gram in grams)
    docs = dict((doc.answer, _cosine_measure(idfs, self._get_tf_idfs(doc))) for
        doc in documents)
    docs = dict((key, val) for key, val in docs.items() if val)
    session.commit()
    try:
        max_ratio = max(docs.values())
        answers = [answer for answer in docs.keys() if docs.get(answer) ==
            max_ratio]
        answer = random.choice(answers)
        logger.debug('{0} -> {1} ({2})'.format(query, answer, max_ratio))
        return answer, max_ratio
    except ValueError:
        raise NoAnswerError('Can not found answer')
    finally:
        session.commit()