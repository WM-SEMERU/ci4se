async def main():
    redis = await aioredis.create_redis('redis://localhost')
    await redis.mset('key:1', 'value1', 'key:2', 'value2')
    cur = b'0'
    while cur:
        cur, keys = await redis.scan(cur, match='key:*')
        print('Iteration results:', keys)
    redis.close()
    await redis.wait_closed()