def answer_options(self):
    return [AnswerOption(element) for element in self._answer_option_xpb.
        apply_(self._question_element)]