def create_store_prompt(name):

    def _prompt(questions, answers=None, **kwargs):
        stored_answers = _read_stored_answers(name)
        to_store = []
        for q in questions:
            if 'store' in q:
                if q.pop('store'):
                    to_store.append(q['name'])
                    if q['name'] in stored_answers:
                        q['default'] = stored_answers[q['name']]
        answers = prompt(questions, answers, **kwargs)
        if to_store:
            for s in to_store:
                if s in answers:
                    stored_answers[s] = answers[s]
            _store_answers(name, stored_answers)
        return answers
    return _prompt