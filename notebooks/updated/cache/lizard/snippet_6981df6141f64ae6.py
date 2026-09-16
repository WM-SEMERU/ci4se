def __process_username_password(self):
    if self.use_username_password_store is not None:
        if self.args.clear_store:
            with load_config(sections=AUTH_SECTIONS) as config:
                config.remove_option(AUTH_SECTION, 'username')
        if not self.args.username:
            self.args.username = get_username(use_store=self.
                use_username_password_store)
        if self.args.clear_store:
            remove_password(AUTH_SECTION, username=self.args.username)
        if not self.args.password:
            self.args.password = get_password(AUTH_SECTION, username=self.
                args.username)
            if self.use_username_password_store:
                save_password(AUTH_SECTION, self.args.password, self.args.
                    username)