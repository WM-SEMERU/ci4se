def delete_user(self, login=None, envs=[], query='/users/'):
    juicer.utils.Log.log_debug('Delete User: %s', login)
    for env in envs:
        if envs.index(env) != 0 and juicer.utils.env_same_host(env, envs[
            envs.index(env) - 1]):
            juicer.utils.Log.log_info(
                'environment `%s` shares a host with environment `%s`... skipping!'
                , (env, envs[envs.index(env) - 1]))
            continue
        elif not juicer.utils.user_exists_p(login, self.connectors[env]):
            juicer.utils.Log.log_info(
                "user `%s` doesn't exist in %s... skipping!", (login, env))
            continue
        else:
            url = '%s%s/' % (query, login)
            _r = self.connectors[env].delete(url)
            if _r.status_code == Constants.PULP_DELETE_OK:
                juicer.utils.Log.log_info('deleted user `%s` in %s', (login,
                    env))
            else:
                _r.raise_for_status()
    return True