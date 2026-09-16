def get_course_id(self, course_uuid):
    course_data = self.get('courseguide/course?uuid={uuid}'.format(uuid=
        course_uuid or self.course_id), params=None)
    try:
        return course_data['response']['docs'][0]['id']
    except KeyError:
        failure_message = 'KeyError in get_course_id - got {0}'.format(
            course_data)
        log.exception(failure_message)
        raise PyLmodUnexpectedData(failure_message)
    except TypeError:
        failure_message = 'TypeError in get_course_id - got {0}'.format(
            course_data)
        log.exception(failure_message)
        raise PyLmodUnexpectedData(failure_message)