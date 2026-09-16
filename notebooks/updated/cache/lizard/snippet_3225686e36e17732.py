def GET_AUTH(self, courseid, taskid):
    course, task = self.get_course_and_check_rights(courseid, taskid)
    return self.page(course, task)