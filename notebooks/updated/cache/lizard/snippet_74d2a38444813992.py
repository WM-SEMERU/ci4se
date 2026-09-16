def get_response(self, question_id):
    question_map = self._get_question_map(question_id)
    return self._get_response_from_question_map(question_map)