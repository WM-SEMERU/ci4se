def update_confirmation_comment(self, confirmation_comment_id,
    confirmation_comment_dict):
    return self._create_put_request(resource=CONFIRMATION_COMMENTS,
        billomat_id=confirmation_comment_id, send_data=
        confirmation_comment_dict)