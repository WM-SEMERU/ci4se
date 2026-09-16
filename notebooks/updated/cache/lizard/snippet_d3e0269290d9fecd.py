def update_email_template(self, template_id, template_dict):
    return self._create_put_request(resource=EMAIL_TEMPLATES, billomat_id=
        template_id, send_data=template_dict)