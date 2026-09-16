def offer_answer(pool, answer, rationale, student_id, algo, options):
    if algo['name'] == 'simple':
        offer_simple(pool, answer, rationale, student_id, options)
    elif algo['name'] == 'random':
        offer_random(pool, answer, rationale, student_id, options)
    else:
        raise UnknownChooseAnswerAlgorithm()