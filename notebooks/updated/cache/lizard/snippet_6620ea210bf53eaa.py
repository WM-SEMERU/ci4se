def get_stories(label_type):
    prefixes = get_story_prefixes(label_type)
    texts = list(set([prefix.split('.')[0].split('/')[1] for prefix in
        prefixes]))
    return texts