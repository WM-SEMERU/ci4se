def validate_seeded_answers(answers, options, algo):
    if algo['name'] == 'simple':
        return validate_seeded_answers_simple(answers, options, algo)
    elif algo['name'] == 'random':
        return validate_seeded_answers_random(answers)
    else:
        raise UnknownChooseAnswerAlgorithm()