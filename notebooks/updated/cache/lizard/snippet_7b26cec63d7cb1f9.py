def admin_emails(doc):
    if doc.get('type') == 'user' and doc.get('state') != 'deactivated':
        if doc.get('role') == 'administrator':
            yield None, doc['email']
        for org_id, state in doc.get('organisations', {}).items():
            if state.get('role') == 'administrator' and state.get('state'
                ) != 'deactivated':
                yield org_id, doc['email']