def get_number(self, question, min_i=float('-inf'), max_i=float('inf'),
    just_these=None):
    try:
        user_answer = self.get_answer(question)
        user_answer = float(user_answer)
        if min_i < user_answer < max_i:
            if just_these:
                if user_answer in just_these:
                    return user_answer
                exc = 'Number cannot be accepted. Just these: '
                exc += str(just_these)
                raise Exception(exc)
            return user_answer
        exc = 'Number is not within limits. '
        exc += 'Min is ' + str(min_i) + '. Max is ' + str(max_i) + ''
        raise Exception(exc)
    except Exception as exc:
        print(str(exc))
        return self.get_number(self.last_question, min_i=min_i, max_i=max_i,
            just_these=just_these)