def GET_AUTH(self, courseid, classroomid):
    course, __ = self.get_course_and_check_rights(courseid, allow_all_staff
        =True)
    if course.is_lti():
        raise web.notfound()
    student_list, tutor_list, other_students, users_info = self.get_user_lists(
        course, classroomid)
    classroom = self.database.classrooms.find_one({'_id': ObjectId(
        classroomid), 'courseid': courseid})
    if classroom:
        return self.template_helper.get_renderer().course_admin.edit_classroom(
            course, student_list, tutor_list, other_students, users_info,
            classroom, '', False)
    else:
        raise web.notfound()