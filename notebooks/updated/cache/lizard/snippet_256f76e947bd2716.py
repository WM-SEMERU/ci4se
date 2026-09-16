def del_all_svc_comments(self, service):
    comments = list(service.comments.keys())
    for uuid in comments:
        service.del_comment(uuid)
    self.send_an_element(service.get_update_status_brok())