def confirm(statement):
    prompt = '{statement} [y/n]'.format(statement=statement)
    answer = _ask(prompt, limited_to=['yes', 'no', 'y', 'n'])
    return answer and answer.startswith('y')