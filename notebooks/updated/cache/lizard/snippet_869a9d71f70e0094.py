def get_semester_title(self, node: BaseNode):
    log.debug('Getting Semester Title for %s' % node.course.id)
    return self._get_semester_from_id(node.course.semester)