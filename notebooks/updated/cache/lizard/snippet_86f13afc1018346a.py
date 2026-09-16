def create_embedded_template_draft(self, client_id, signer_roles, test_mode
    =False, files=None, file_urls=None, title=None, subject=None, message=
    None, cc_roles=None, merge_fields=None, use_preexisting_fields=False):
    params = {'test_mode': test_mode, 'client_id': client_id, 'files':
        files, 'file_urls': file_urls, 'title': title, 'subject': subject,
        'message': message, 'signer_roles': signer_roles, 'cc_roles':
        cc_roles, 'merge_fields': merge_fields, 'use_preexisting_fields':
        use_preexisting_fields}
    return self._create_embedded_template_draft(**params)