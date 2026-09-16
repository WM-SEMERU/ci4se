def _populate_user_from_dn_regex(self):
    for field, regex in self.settings.USER_FLAGS_BY_DN_REGEX.items():
        field_value = False
        if re.search(regex, self._get_user_dn(), re.IGNORECASE):
            field_value = True
        setattr(self._user, field, field_value)