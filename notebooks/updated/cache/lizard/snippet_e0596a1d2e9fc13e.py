def user_unicode(self):
    if self.email:
        shortened = self.email.split('@')[0]
        return '%s %s (%s@...)' % (self.first_name, self.last_name, shortened)
    elif self.first_name or self.last_name:
        return '%s %s' % (self.first_name, self.last_name)
    elif self.username:
        return '%s' % self.username
    else:
        return 'User %u' % self.pk