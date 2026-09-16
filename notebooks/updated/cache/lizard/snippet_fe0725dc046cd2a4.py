def json_changepass(self):
    post_data = self.get_post_data()
    check_usr_status = MUser.check_user(self.userinfo.uid, post_data['rawpass']
        )
    if check_usr_status == 1:
        user_create_status = self.__check_valid_pass(post_data)
        if not user_create_status['success']:
            return json.dump(user_create_status, self)
        form_pass = SumFormPass(self.request.arguments)
        if form_pass.validate():
            MUser.update_pass(self.userinfo.uid, post_data['user_pass'])
            return json.dump(user_create_status, self)
        return json.dump(user_create_status, self)
    return False