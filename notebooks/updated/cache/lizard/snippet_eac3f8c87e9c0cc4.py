def grading_value_text(self):
    if self.assignment.is_graded():
        if self.is_grading_finished():
            return str(self.grading)
        else:
            return str('pending')
    elif self.is_grading_finished():
        return str('done')
    else:
        return str('not done')