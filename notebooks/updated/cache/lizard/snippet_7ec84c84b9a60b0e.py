def time(self, id=None, nome=None, slug=None, as_json=False):
    if not any((id, nome, slug)):
        raise CartolaFCError(
            'Você precisa informar o nome ou o slug do time que deseja obter')
    param = 'id' if id else 'slug'
    value = id if id else slug if slug else convert_team_name_to_slug(nome)
    url = '{api_url}/time/{param}/{value}'.format(api_url=self._api_url,
        param=param, value=value)
    data = self._request(url)
    if bool(as_json):
        return data
    clubes = {clube['id']: Clube.from_dict(clube) for clube in data[
        'clubes'].values()}
    return Time.from_dict(data, clubes=clubes, capitao=data['capitao_id'])