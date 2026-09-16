def get_course(self, course, use_sis_id=False, **kwargs):
    if use_sis_id:
        course_id = course
        uri_str = 'courses/sis_course_id:{}'
    else:
        course_id = obj_or_id(course, 'course', (Course,))
        uri_str = 'courses/{}'
    response = self.__requester.request('GET', uri_str.format(course_id),
        _kwargs=combine_kwargs(**kwargs))
    return Course(self.__requester, response.json())