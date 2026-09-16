def get_klout_topics(tweet, topic_type='influence'):
    try:
        if is_original_format(tweet):
            topics = tweet['user']['derived']['klout']['{}_topics'.format(
                topic_type)]
        else:
            topics = tweet['gnip']['klout_profile']['topics']
    except KeyError:
        return None
    topics_list = []
    if is_original_format(tweet):
        for topic in topics:
            this_topic = dict(url=topic['url'], id=topic['id'], name=topic[
                'name'], score=topic['score'])
            topics_list.append(this_topic)
    else:
        relevant_topics = [x for x in topics if x['topic_type'] == topic_type]
        for topic in relevant_topics:
            this_topic = dict(url=topic['link'], id=topic['id'], name=topic
                ['displayName'], score=topic['score'])
            topics_list.append(this_topic)
    sorted_topics_list = sorted(topics_list, key=lambda x: x['score'])
    return sorted_topics_list