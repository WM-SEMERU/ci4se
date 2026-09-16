def topic_pages_inline_list(topic):
    data_dict = {'topic': topic}
    pages_number = (topic.posts_count - 1
        ) // machina_settings.TOPIC_POSTS_NUMBER_PER_PAGE + 1
    if pages_number > 5:
        data_dict['first_pages'] = range(1, 5)
        data_dict['last_page'] = pages_number
    elif pages_number > 1:
        data_dict['first_pages'] = range(1, pages_number + 1)
    return data_dict