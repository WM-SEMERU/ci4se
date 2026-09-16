def update_beliefs(self, corpus_id):
    corpus = self.get_corpus(corpus_id)
    be = BeliefEngine(self.scorer)
    stmts = list(corpus.statements.values())
    be.set_prior_probs(stmts)
    for uuid, correct in corpus.curations.items():
        stmt = corpus.statements.get(uuid)
        if stmt is None:
            logger.warning('%s is not in the corpus.' % uuid)
            continue
        stmt.belief = correct
    belief_dict = {st.uuid: st.belief for st in stmts}
    return belief_dict