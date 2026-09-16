async def endorsements(self, root):
    text = root.find('ENDORSEMENTS').text
    return [Nation(name) for name in text.split(',')] if text else []