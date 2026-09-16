def user_bindings(self):
    if self._user_bindings is None:
        self._user_bindings = UserBindingList(self._version, service_sid=
            self._solution['service_sid'], user_sid=self._solution['sid'])
    return self._user_bindings