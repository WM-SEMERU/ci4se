def find_attractiveness(self, username, accuracy=1000, _lower=0, _higher=10000
    ):
    average = (_higher + _lower) // 2
    if _higher - _lower <= accuracy:
        return average
    results = search(self._session, count=9, gentation='everybody',
        keywords=username, attractiveness_min=average, attractiveness_max=
        _higher)
    found_match = False
    if results:
        for profile in results:
            if profile.username.lower() == username:
                found_match = True
                break
    if found_match:
        return self.find_attractiveness(username, accuracy, average, _higher)
    else:
        return self.find_attractiveness(username, accuracy, _lower, average)