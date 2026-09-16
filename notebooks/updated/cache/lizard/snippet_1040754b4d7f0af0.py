def update_profile(self, about_me=None, display_name=None, email=None,
    first_name=None, gender=None, last_name=None, mobile_number=None,
    relationship_status=None, title=None, where_am_i=None, scope=
    'profile/write'):
    data = {}
    if about_me:
        data['AboutMe'] = about_me
    if display_name:
        data['DisplayName'] = display_name
    if email:
        data['Email'] = email
    if first_name:
        data['FirstName'] = first_name
    if gender:
        data['Gender'] = gender
    if last_name:
        data['LastName'] = last_name
    if mobile_number:
        data['MobileNumber'] = mobile_number
    if relationship_status:
        data['RelationshipStatus'] = relationship_status
    if title:
        data['Title'] = title
    if where_am_i:
        data['WhereAmI'] = where_am_i
    if data:
        _put(token=self.oauth.get_user_token(scope), uri='/user/profile',
            data=data)