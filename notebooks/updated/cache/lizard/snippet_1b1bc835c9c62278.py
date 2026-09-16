def recent(self, with_catalog=True, with_date=True):
    kwd = {'pager': '', 'title': 'Recent posts.', 'with_catalog':
        with_catalog, 'with_date': with_date}
    self.render('list/post_list.html', kwd=kwd, view=MPost.query_recent(num
        =20), postrecs=MPost.query_recent(num=2), format_date=tools.
        format_date, userinfo=self.userinfo, cfg=CMS_CFG)