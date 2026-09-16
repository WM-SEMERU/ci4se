def get_student_enrollments(self):
    resp = self.requester.get(urljoin(self.base_url, self.enrollment_url))
    resp.raise_for_status()
    return Enrollments(resp.json())