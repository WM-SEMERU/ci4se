def POST(self, courseid):
    course = self.get_course(courseid)
    user_input = web.input()
    if 'unregister' in user_input and course.allow_unregister():
        self.user_manager.course_unregister_user(course, self.user_manager.
            session_username())
        raise web.seeother(self.app.get_homepath() + '/mycourses')
    return self.show_page(course)