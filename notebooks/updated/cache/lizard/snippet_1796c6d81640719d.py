def validate(self):
    try:
        assert self.question == '', 'Assumption Failed: Perseus question should not have a question'
        assert self.question_type == exercises.PERSEUS_QUESTION, 'Assumption Failed: Question should be perseus type'
        assert self.answers == [
            ], 'Assumption Failed: Answer list should be empty for perseus question'
        assert self.hints == [
            ], 'Assumption Failed: Hints list should be empty for perseus question'
        return super(PerseusQuestion, self).validate()
    except AssertionError as ae:
        raise InvalidQuestionException('Invalid question: {0}'.format(self.
            __dict__))