def get_student_certificate(self, username, course_id):
    resp = self.requester.get(urljoin(self.base_url,
        '/api/certificates/v0/certificates/{username}/courses/{course_key}/'
        .format(username=username, course_key=course_id)))
    resp.raise_for_status()
    return Certificate(resp.json())