def is_complete(self):
    self._update_questions()
    for question_map in self._my_map['questions']:
        if 'missingResponse' in question_map['responses'][0]:
            return False
    return True