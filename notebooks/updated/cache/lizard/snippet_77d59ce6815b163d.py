def get_yes_no(self, question):
    user_answer = self.get_answer(question).lower()
    if user_answer in self.yes_input:
        return True
    if user_answer in self.no_input:
        return False
    is_yes = self.is_yes(user_answer)
    is_no = self.is_no(user_answer)
    if is_yes and not is_no:
        return True
    if is_no and not is_yes:
        return False
    if self.interactive:
        self.show_help()
        return self.get_yes_no(self.last_question)
    return False