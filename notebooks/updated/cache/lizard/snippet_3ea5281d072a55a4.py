def user_with_student_id(self, student_id):
    results = User.objects.filter(student_id=student_id)
    if len(results) == 1:
        return results.first()
    return None