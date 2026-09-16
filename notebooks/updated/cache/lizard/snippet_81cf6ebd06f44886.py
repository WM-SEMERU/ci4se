async def main():
    async with aiohttp.ClientSession() as session:
        data = Glances(loop, session, version=VERSION)
        await data.get_metrics('mem')
        print('Memory values:', data.values)
        await data.get_metrics('diskio')
        print('Disk values:', data.values)