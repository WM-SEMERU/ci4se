def logout(self, redirect_to='/'):

    def _logout(env, data):
        location = redirect_to
        if location is None and env.request.referer:
            location = env.request.referer
        elif location is None:
            location = '/'
        response = HTTPSeeOther(location=str(location))
        self.logout_user(env.request, response)
        return response
    return web.match('/logout', 'logout') | web.method('post') | _logout