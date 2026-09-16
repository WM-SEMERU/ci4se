def create_milestone(self, project_id, title, deadline, party_id, notify):
    path = '/projects/%u/milestones/create' % project_id
    req = ET.Element('request')
    req.append(self._create_milestone_elem(title, deadline, party_id, notify))
    return self._request(path, req)