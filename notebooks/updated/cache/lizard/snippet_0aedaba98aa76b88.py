def return_current_uri_subpage(self):
    uri = post_slash('%s%s/%s/%s' % (post_slash(self.current_dir()), self.
        slots['page'], self.slots['item'], self.slots['subpage']))
    return uri