def __could_edit(self, slug):
    page_rec = MWiki.get_by_uid(slug)
    if not page_rec:
        return False
    if self.check_post_role()['EDIT']:
        return True
    elif page_rec.user_name == self.userinfo.user_name:
        return True
    else:
        return False