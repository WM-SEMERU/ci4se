def _send(self, message, fail_silently=False):
    seeds = '1234567890qwertyuiopasdfghjklzxcvbnm'
    file_part1 = datetime.now().strftime('%Y%m%d%H%M%S')
    file_part2 = ''.join(sample(seeds, 4))
    filename = join(self.tld, '%s_%s.msg' % (file_part1, file_part2))
    with open(filename, 'w') as fd:
        fd.write(str(message.to_message()))