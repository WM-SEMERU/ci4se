def get_ytvideos(query, ilogger):
    queue = []
    search_result = ytdiscoveryapi.search().list(q=query, part='id,snippet',
        maxResults=1, type='video,playlist').execute()
    if not search_result['items']:
        return []
    title = search_result['items'][0]['snippet']['title']
    ilogger.info('Queueing {}'.format(title))
    if search_result['items'][0]['id']['kind'] == 'youtube#video':
        videoid = search_result['items'][0]['id']['videoId']
        queue.append(['https://www.youtube.com/watch?v={}'.format(videoid),
            title])
    elif search_result['items'][0]['id']['kind'] == 'youtube#playlist':
        queue = get_queue_from_playlist(search_result['items'][0]['id'][
            'playlistId'])
    return queue