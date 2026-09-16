def get_question_answer_id(self, question, fast=False, bust_questions_cache
    =False):
    if hasattr(question, 'answer_id'):
        return question.answer_id
    user_question = self.get_user_question(question, fast=fast,
        bust_questions_cache=bust_questions_cache)
    return user_question.get_answer_id_for_question(question)