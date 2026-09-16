def add_page(self, slug):
    post_data = self.get_post_data()
    post_data['user_name'] = self.userinfo.user_name
    if MWiki.get_by_uid(slug):
        self.set_status(400)
        return False
    else:
        MWiki.create_page(slug, post_data)
        tornado.ioloop.IOLoop.instance().add_callback(self.cele_gen_whoosh)
        self.redirect('/page/{0}'.format(slug))