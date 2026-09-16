def _add_user_to_file(file_id, service, user_email, perm_type='user', role=
    'writer'):
    new_permission = {'value': user_email, 'type': perm_type, 'role': role}
    try:
        service.permissions().insert(fileId=file_id, body=new_permission
            ).execute()
    except errors.HttpError as error:
        show_error('An error adding users to spreadsheet: {0}'.format(error))