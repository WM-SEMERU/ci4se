def to_array(self):
    array = super(InputContactMessageContent, self).to_array()
    array['phone_number'] = u(self.phone_number)
    array['first_name'] = u(self.first_name)
    if self.last_name is not None:
        array['last_name'] = u(self.last_name)
    if self.vcard is not None:
        array['vcard'] = u(self.vcard)
    return array