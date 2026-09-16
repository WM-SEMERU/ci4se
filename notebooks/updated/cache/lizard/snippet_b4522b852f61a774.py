def raw_mentions(self):
    return [int(x) for x in re.findall('<@!?([0-9]+)>', self.content)]