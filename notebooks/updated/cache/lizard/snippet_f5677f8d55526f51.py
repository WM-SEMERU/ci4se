def get_user_by_email(self, email):
    results = self.get_users(filter='email eq "%s"' % email)
    if results['totalResults'] == 0:
        logging.warning('Found no matches for given email.')
        return
    elif results['totalResults'] > 1:
        logging.warning('Found %s matches for email %s' % (results[
            'totalResults'], email))
    return results['resources'][0]