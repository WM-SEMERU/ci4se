def get_unique_clause_indices(text):
    if not text.is_tagged(CLAUSES):
        text.tag_clauses()
    clause_indices = []
    sent_id = 0
    for sub_text in text.split_by(SENTENCES):
        for word, cl_index in zip(sub_text.words, sub_text.clause_indices):
            clause_indices.append(sent_id + cl_index)
        nr_of_clauses = len(set(sub_text.clause_indices))
        sent_id += nr_of_clauses
    assert len(clause_indices) == len(text.words
        ), '(!) Number of clause indices should match nr of words!'
    return clause_indices