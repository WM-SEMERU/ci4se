def create_connection():
    redis_url = os.getenv('REDIS_URL')
    if not redis_url:
        redis_url = 'redis://localhost:6379'
    urlparse.uses_netloc.append('redis')
    url = urlparse.urlparse(redis_url)
    return redis.StrictRedis(host=url.hostname, port=url.port, db=0,
        password=url.password)