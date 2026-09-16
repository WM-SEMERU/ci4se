def POST_AUTH(self):
    username = self.user_manager.session_username()
    user_info = self.database.users.find_one({'username': username})
    user_input = web.input()
    success = None
    if 'register_courseid' in user_input and user_input['register_courseid'
        ] != '':
        try:
            course = self.course_factory.get_course(user_input[
                'register_courseid'])
            if not course.is_registration_possible(user_info):
                success = False
            else:
                success = self.user_manager.course_register_user(course,
                    username, user_input.get('register_password', None))
        except:
            success = False
    elif 'new_courseid' in user_input and self.user_manager.user_is_superadmin(
        ):
        try:
            courseid = user_input['new_courseid']
            self.course_factory.create_course(courseid, {'name': courseid,
                'accessible': False})
            success = True
        except:
            success = False
    return self.show_page(success)