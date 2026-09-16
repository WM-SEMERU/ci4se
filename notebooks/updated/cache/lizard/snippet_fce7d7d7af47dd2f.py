def to_array(self):
    array = super(Contact, self).to_array()
    array['phone_number'] = u(self.phone_number)
    array['first_name'] = u(self.first_name)
    if self.last_name is not None:
        array['last_name'] = u(self.last_name)
    if self.user_id is not None:
        array['user_id'] = int(self.user_id)
    if self.vcard is not None:
        array['vcard'] = u(self.vcard)
    return array