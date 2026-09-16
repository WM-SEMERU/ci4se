def name(self):
    if 'lis_person_sourcedid' in self.session:
        return self.session['lis_person_sourcedid']
    elif 'lis_person_contact_email_primary' in self.session:
        return self.session['lis_person_contact_email_primary']
    elif 'user_id' in self.session:
        return self.session['user_id']
    else:
        return ''