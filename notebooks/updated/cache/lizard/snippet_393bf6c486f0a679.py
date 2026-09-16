def lesson_nums(self):
    lesson_nums = {}
    for brain_name, curriculum in self.brains_to_curriculums.items():
        lesson_nums[brain_name] = curriculum.lesson_num
    return lesson_nums