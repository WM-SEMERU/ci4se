def create_variables(self, courses):
    has_sections = isinstance(courses, dict)
    for course in courses:
        self.p.add_variable(course, courses.get(course, []) if has_sections
             else self.get_sections(course))