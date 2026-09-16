def check_submission(self, submission_string, submission_id):
    if self.question_upload_type == STRING:
        return self.question_answer_string.lower().replace(' ', ''
            ) == submission_string.lower().replace(' ', '')
    else:
        raise Exception('Question not String Type.')