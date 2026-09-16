def load_post(wp_post_id):
    time.sleep(1)
    loader = WPAPILoader()
    post = loader.load_post(wp_post_id)
    if post:
        logger.info('Successfully loaded post wp_post_id=%s, pk=%s',
            wp_post_id, post.pk)
    else:
        logger.warning('Error loading post wp_post_id=%s', wp_post_id)