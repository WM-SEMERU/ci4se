def add(self, post_id):
    post_data = self.get_post_data()
    post_data['user_name'] = self.userinfo.user_name
    post_data['user_id'] = self.userinfo.uid
    post_data['post_id'] = post_id
    replyid = MReply.create_reply(post_data)
    if replyid:
        out_dic = {'pinglun': post_data['cnt_reply'], 'uid': replyid}
        logger.info('add reply result dic: {0}'.format(out_dic))
        return json.dump(out_dic, self)