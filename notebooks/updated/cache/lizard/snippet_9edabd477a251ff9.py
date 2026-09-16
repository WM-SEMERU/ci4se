def __create_channel_run(self, channel, username, token):
    data = {'channel_id': channel.get_node_id().hex, 'chef_name': self.
        __get_chef_name(), 'ricecooker_version': __version__,
        'started_by_user': username, 'started_by_user_token': token,
        'content_server': config.DOMAIN}
    try:
        response = requests.post(config.sushi_bar_channel_runs_url(), data=
            data, auth=AUTH)
        response.raise_for_status()
        return response.json()['run_id']
    except Exception as e:
        config.LOGGER.error('Error channel run: %s' % e)
    return None