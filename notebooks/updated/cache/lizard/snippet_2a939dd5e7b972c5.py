def list_courses(self):
    reply = get_page(self._session, OPENCOURSE_MEMBERSHIPS, json=True)
    course_list = reply['linked']['courses.v1']
    slugs = [element['slug'] for element in course_list]
    return slugs